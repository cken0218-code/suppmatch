"""
ASX Watchlist - High Potential Australian Stocks
Researched and curated based on fundamentals, momentum, and catalysts

Sectors: Technology, Mining, Healthcare, Energy
"""

ASX_WATCHLIST = {
    "version": "2026-02-20",
    "last_updated": "2026-02-20",
    
    "stocks": {
        # === TECHNOLOGY ===
        "WBT": {
            "name": "Weebit Nano",
            "sector": "Technology",
            "industry": "Semiconductors",
            "market_cap": "Mid-cap",
            "fundamentals": {
                "pe_ratio": None,  # Pre-revenue/early growth
                "growth_rate": "High",
                "revenue_trend": "Growing with new licensees"
            },
            "catalysts": [
                "Texas Instruments partnership (Jan 2026)",
                "FY26 revenue target of $10M",
                "Commercialization of ReRAM technology",
                "Multiple foundry/IDM partnerships"
            ],
            "risk_level": "High",
            "analyst_rating": "Buy",
            "notes": "Most advanced ASX semiconductor stock. ReRAM technology could replace flash memory."
        },
        "WTC": {
            "name": "WiseTech Global",
            "sector": "Technology",
            "industry": "Logistics Software",
            "market_cap": "Large-cap",
            "fundamentals": {
                "pe_ratio": "~50-60",
                "growth_rate": "High",
                "revenue_trend": "Strong SaaS growth"
            },
            "catalysts": [
                "Global logistics demand growth",
                "M&A opportunities",
                "Geographic expansion"
            ],
            "risk_level": "Medium",
            "analyst_rating": "Buy",
            "notes": "Dominant logistics software provider with strong SaaS recurring revenue."
        },
        "XRO": {
            "name": "Xero",
            "sector": "Technology",
            "industry": "Accounting Software",
            "market_cap": "Large-cap",
            "fundamentals": {
                "pe_ratio": "~80+",
                "growth_rate": "High",
                "revenue_trend": "Strong subscriber growth"
            },
            "catalysts": [
                "SME digital transformation",
                "International expansion",
                "AI integration opportunities"
            ],
            "risk_level": "Medium",
            "analyst_rating": "Buy",
            "notes": "Leading cloud accounting platform for small businesses globally."
        },
        "ABB": {
            "name": "Aussie Broadband",
            "sector": "Technology",
            "industry": "Telecommunications",
            "market_cap": "Mid-cap",
            "fundamentals": {
                "pe_ratio": "~20-25",
                "growth_rate": "High",
                "revenue_trend": "FY25: $1.2B (+19%), EBITDA $55.8M"
            },
            "catalysts": [
                "FY26 EBITDA guidance: $157-167M (+14-21%)",
                "NBN contract growth",
                "Enterprise segment expansion"
            ],
            "risk_level": "Medium",
            "analyst_rating": "Buy",
            "notes": "Fast-growing telco with industry-leading customer service reputation."
        },
        "OCL": {
            "name": "Objective Corporation",
            "sector": "Technology",
            "industry": "Government Software",
            "market_cap": "Mid-cap",
            "fundamentals": {
                "pe_ratio": "~30-35",
                "growth_rate": "Medium-High",
                "revenue_trend": "FY25: $123.5M (+5%), Profit $35.4M (+13%)"
            },
            "catalysts": [
                "FY26 target: ~15% ARR growth",
                "AI-enabled product enhancements",
                "Public sector spending growth"
            ],
            "risk_level": "Medium",
            "analyst_rating": "Buy",
            "notes": "Profitable government/business software with strong recurring revenue."
        },
        
        # === MINING ===
        "SFR": {
            "name": "Sandfire",
            "sector": "Mining",
            "industry": "Copper",
            "market_cap": "Large-cap",
            "fundamentals": {
                "pe_ratio": "~8-12",
                "growth_rate": "Medium",
                "revenue_trend": "MATSA mine: 150kt+ FY25"
            },
            "catalysts": [
                "Copper predicted as commodity of 2026",
                "MATSA mine production growth",
                "Black Butte PFS (USA)",
                "A1 maiden reserve (Botswana)"
            ],
            "risk_level": "Medium",
            "analyst_rating": "Buy",
            "notes": "Premium copper play. Copper demand from AI, EVs, data centers, clean energy."
        },
        "IPD": {
            "name": "IPD Group",
            "sector": "Mining",
            "industry": "Electrical Equipment",
            "market_cap": "Small-cap",
            "fundamentals": {
                "pe_ratio": "~15-20",
                "growth_rate": "Medium-High",
                "revenue_trend": "Acquisition-driven growth"
            },
            "catalysts": [
                "Platinum Cables acquisition (mining cables)",
                "Data center boom",
                "EV charging infrastructure demand",
                "Australian power consumption growth"
            ],
            "risk_level": "Medium-High",
            "analyst_rating": "Buy",
            "notes": "Electrical equipment distributor benefiting from mining and energy infrastructure."
        },
        "FMG": {
            "name": "Fortescue",
            "sector": "Mining",
            "industry": "Iron Ore",
            "market_cap": "Large-cap",
            "fundamentals": {
                "pe_ratio": "~6-8",
                "growth_rate": "Medium",
                "revenue_trend": "Strong iron ore volumes"
            },
            "catalysts": [
                "Green energy push (Fortescue Future Industries)",
                "Strong iron ore prices",
                "Debt reduction progress"
            ],
            "risk_level": "Medium",
            "analyst_rating": "Hold",
            "notes": "Major iron ore producer with green energy diversification strategy."
        },
        
        # === HEALTHCARE ===
        "CSL": {
            "name": "CSL Limited",
            "sector": "Healthcare",
            "industry": "Biopharma",
            "market_cap": "Large-cap",
            "fundamentals": {
                "pe_ratio": "~25-30",
                "growth_rate": "Medium",
                "revenue_trend": "Stable with growth in Seqirus"
            },
            "catalysts": [
                "Vifor integration complete",
                "Flu vaccine demand",
                "Plasma collection expansion"
            ],
            "risk_level": "Low-Medium",
            "analyst_rating": "Buy",
            "notes": "Global biopharma leader with strong immunology and vaccine franchises."
        },
        "EBR": {
            "name": "EBR Systems",
            "sector": "Healthcare",
            "industry": "Medical Devices",
            "market_cap": "Small-cap",
            "fundamentals": {
                "pe_ratio": None,
                "growth_rate": "High",
                "revenue_trend": "FDA approved 2025, early sales in 2026"
            },
            "catalysts": [
                "FDA approval obtained 2025",
                "WiSE system commercialization",
                "US$4B+ addressable market",
                "Abbott partnership trial"
            ],
            "risk_level": "High",
            "analyst_rating": "Speculative Buy",
            "notes": "Wireless cardiac pacing technology. FDA approved, scaling sales in 2026."
        },
        "BB1": {
            "name": "BlinkLab",
            "sector": "Healthcare",
            "industry": "Digital Health",
            "market_cap": "Small-cap",
            "fundamentals": {
                "pe_ratio": None,
                "growth_rate": "High",
                "revenue_trend": "Pre-revenue, clinical trial phase"
            },
            "catalysts": [
                "FDA clinical trial 2026",
                "CE Mark approval targeted 2026",
                "ADHD/autism diagnostic platform"
            ],
            "risk_level": "Very High",
            "analyst_rating": "Speculative Buy",
            "notes": "Digital biomarker platform for ADHD/autism diagnosis using computer vision."
        },
        
        # === ENERGY & RESOURCES ===
        "EOS": {
            "name": "EOS",
            "sector": "Energy",
            "industry": "Defense Technology",
            "market_cap": "Mid-cap",
            "fundamentals": {
                "pe_ratio": "~30-40",
                "growth_rate": "High",
                "revenue_trend": "Defense contracts growing"
            },
            "catalysts": [
                "100kW laser weapon export to NATO country",
                "Defense spending boost globally",
                "Global expansion (US, Middle East, Europe)"
            ],
            "risk_level": "Medium",
            "analyst_rating": "Buy",
            "notes": "Defense tech leader. First export of 100kW anti-drone laser system."
        },
        "NST": {
            "name": "Northern Star",
            "sector": "Mining",
            "industry": "Gold",
            "market_cap": "Large-cap",
            "fundamentals": {
                "pe_ratio": "~10-15",
                "growth_rate": "Medium",
                "revenue_trend": "Strong gold production"
            },
            "catalysts": [
                "Gold price strength",
                "KCGM expansion project",
                "Super Pit growth"
            ],
            "risk_level": "Medium",
            "analyst_rating": "Buy",
            "notes": "Tier-1 gold miner with strong production profile and growth projects."
        }
    },
    
    "sector_summary": {
        "Technology": {
            "outlook": "Positive",
            "drivers": ["AI adoption", "Digital transformation", "SaaS growth"],
            "top_picks": ["WBT", "ABB", "OCL"]
        },
        "Mining": {
            "outlook": "Positive",
            "drivers": ["Copper demand (AI/EVs)", "Gold price", "Critical minerals"],
            "top_picks": ["SFR", "NST"]
        },
        "Healthcare": {
            "outlook": "Neutral-Positive",
            "drivers": ["Aging population", "Digital health", "Medical innovation"],
            "top_picks": ["CSL", "EBR"]
        },
        "Energy": {
            "outlook": "Positive",
            "drivers": ["Defense spending", "Energy security", "Technology upgrades"],
            "top_picks": ["EOS"]
        }
    }
}

def get_watchlist_summary():
    """Get summary of watchlist"""
    summary = []
    summary.append("=" * 60)
    summary.append("ASX WATCHLIST SUMMARY")
    summary.append(f"Last Updated: {ASX_WATCHLIST['last_updated']}")
    summary.append("=" * 60)
    summary.append("")
    
    for ticker, info in ASX_WATCHLIST["stocks"].items():
        summary.append(f"{ticker}: {info['name']} ({info['sector']})")
        summary.append(f"  Rating: {info['analyst_rating']} | Risk: {info['risk_level']}")
        if info['catalysts']:
            summary.append(f"  Key Catalyst: {info['catalysts'][0]}")
        summary.append("")
    
    return "\n".join(summary)

if __name__ == "__main__":
    print(get_watchlist_summary())
