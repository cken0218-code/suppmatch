'use client';

import { useEffect, useMemo, useRef, useState } from 'react';
import { useLocale } from '@/contexts/LocaleContext';
import { getSuggestions, type SearchSuggestion } from '@/data/searchEnhance';
import { symptoms } from '@/data/symptoms';
import { SearchIcon, XIcon } from '@/components/icons';

interface SearchBarProps {
  onSearch: (query: string) => void;
  showHistory: string[];
  onClearHistory: () => void;
  /** Optional: jump category when user picks a category-type suggestion */
  onPickCategory?: (categoryId: string) => void;
}

export function SearchBar({
  onSearch,
  showHistory,
  onClearHistory,
  onPickCategory,
}: SearchBarProps) {
  const { locale, t } = useLocale();
  const [value, setValue] = useState('');
  const [open, setOpen] = useState(false);
  const [highlight, setHighlight] = useState(0);
  const wrapRef = useRef<HTMLDivElement>(null);

  const suggestions = useMemo(() => {
    if (!value.trim()) return [] as SearchSuggestion[];
    const staticOnes = getSuggestions(value, 4);
    // Live symptom names matching the query (current locale)
    const q = value.toLowerCase();
    const live: SearchSuggestion[] = symptoms
      .filter((s) => {
        const n = s.names[locale].toLowerCase();
        const en = s.names.en.toLowerCase();
        return n.includes(q) || en.includes(q);
      })
      .slice(0, 5)
      .map((s) => ({
        text: s.names[locale],
        category: s.category_id,
        type: 'symptom' as const,
      }));

    const seen = new Set<string>();
    const merged: SearchSuggestion[] = [];
    for (const item of [...live, ...staticOnes]) {
      const key = item.text.toLowerCase();
      if (seen.has(key)) continue;
      seen.add(key);
      merged.push(item);
      if (merged.length >= 8) break;
    }
    return merged;
  }, [value, locale]);

  useEffect(() => {
    setHighlight(0);
  }, [suggestions]);

  useEffect(() => {
    function onDocClick(e: MouseEvent) {
      if (!wrapRef.current?.contains(e.target as Node)) setOpen(false);
    }
    document.addEventListener('mousedown', onDocClick);
    return () => document.removeEventListener('mousedown', onDocClick);
  }, []);

  const handleChange = (next: string) => {
    setValue(next);
    onSearch(next);
    setOpen(true);
  };

  const applySuggestion = (item: SearchSuggestion) => {
    if (item.type === 'category' && onPickCategory) {
      onPickCategory(item.category);
      setValue('');
      onSearch('');
    } else {
      setValue(item.text);
      onSearch(item.text);
    }
    setOpen(false);
  };

  const handleKeyDown = (e: React.KeyboardEvent<HTMLInputElement>) => {
    if (!open || suggestions.length === 0) return;
    if (e.key === 'ArrowDown') {
      e.preventDefault();
      setHighlight((h) => (h + 1) % suggestions.length);
    } else if (e.key === 'ArrowUp') {
      e.preventDefault();
      setHighlight((h) => (h - 1 + suggestions.length) % suggestions.length);
    } else if (e.key === 'Enter' && suggestions[highlight]) {
      e.preventDefault();
      applySuggestion(suggestions[highlight]);
    } else if (e.key === 'Escape') {
      setOpen(false);
    }
  };

  const typeLabel = (type: SearchSuggestion['type']) => {
    if (type === 'symptom') return t('search.type.symptom');
    if (type === 'supplement') return t('search.type.supplement');
    return t('search.type.category');
  };

  return (
    <div className="w-full" ref={wrapRef}>
      <div className="relative">
        <div className="pointer-events-none absolute left-4 top-1/2 -translate-y-1/2 text-zinc-500">
          <SearchIcon />
        </div>
        <input
          type="text"
          value={value}
          onChange={(e) => handleChange(e.target.value)}
          onFocus={() => setOpen(true)}
          onKeyDown={handleKeyDown}
          placeholder={t('search.placeholder')}
          className="w-full px-4 py-4 pl-12 pr-12 text-base sm:text-lg bg-surface-elevated border border-surface-border rounded-2xl text-white placeholder:text-zinc-500 focus:border-accent-purple focus:ring-2 focus:ring-accent-purple/30 outline-none transition-all"
          autoComplete="off"
          role="combobox"
          aria-expanded={open && suggestions.length > 0}
          aria-autocomplete="list"
        />
        {value && (
          <button
            type="button"
            onClick={() => handleChange('')}
            className="absolute right-3 top-1/2 -translate-y-1/2 p-1.5 text-zinc-400 hover:text-white hover:bg-surface-card rounded-lg transition-colors"
            aria-label={t('search.clear')}
          >
            <XIcon />
          </button>
        )}

        {open && suggestions.length > 0 && (
          <ul
            role="listbox"
            className="absolute z-20 left-0 right-0 mt-2 bg-surface-elevated border border-surface-border rounded-2xl shadow-2xl shadow-black/40 overflow-hidden max-h-72 overflow-y-auto"
          >
            {suggestions.map((item, idx) => (
              <li key={`${item.type}-${item.text}`}>
                <button
                  type="button"
                  role="option"
                  aria-selected={idx === highlight}
                  onMouseEnter={() => setHighlight(idx)}
                  onClick={() => applySuggestion(item)}
                  className={`w-full flex items-center justify-between gap-3 px-4 py-3 text-left text-sm transition-colors ${
                    idx === highlight
                      ? 'bg-accent-purple/15 text-white'
                      : 'text-zinc-300 hover:bg-surface-card'
                  }`}
                >
                  <span className="truncate font-medium">{item.text}</span>
                  <span className="shrink-0 text-xs text-zinc-500">{typeLabel(item.type)}</span>
                </button>
              </li>
            ))}
          </ul>
        )}
      </div>

      {showHistory.length > 0 && !value && (
        <div className="mt-3 flex items-center gap-2 flex-wrap">
          <span className="text-xs text-zinc-500">{t('search.recent')}</span>
          {showHistory.slice(0, 5).map((item) => (
            <button
              key={item}
              type="button"
              onClick={() => handleChange(item)}
              className="px-2.5 py-1 text-xs bg-surface-card border border-surface-border text-zinc-400 rounded-lg hover:text-white hover:border-zinc-500 transition-colors"
            >
              {item}
            </button>
          ))}
          <button
            type="button"
            onClick={onClearHistory}
            className="text-xs text-zinc-500 hover:text-red-400 transition-colors"
          >
            {t('search.clearHistory')}
          </button>
        </div>
      )}
    </div>
  );
}
