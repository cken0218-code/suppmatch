// Affiliate Platform Configuration
export interface AffiliatePlatform {
  name: string;
  affiliateId: string;
  baseUrl: string;
  commission: string;
  color: string;
  logo: string;
}

const PLACEHOLDER_IDS = new Set(['YOUR_AFF_ID', 'YOUR_AMAZON_TAG', '']);

export const affiliateConfig: Record<string, AffiliatePlatform> = {
  iherb: {
    name: 'iHerb',
    // Prefer NEXT_PUBLIC_ so client components can read it at runtime
    affiliateId:
      process.env.NEXT_PUBLIC_IHERB_AFF_ID ||
      process.env.IHERB_AFF_ID ||
      'MLG10',
    baseUrl: 'https://www.iherb.com',
    commission: '5-15%',
    color: '#40AF6E',
    logo: '🌿',
  },
  amazon: {
    name: 'Amazon',
    affiliateId:
      process.env.NEXT_PUBLIC_AMAZON_AFF_ID ||
      process.env.AMAZON_AFF_ID ||
      '',
    baseUrl: 'https://www.amazon.com',
    commission: '3-10%',
    color: '#FF9900',
    logo: '📦',
  },
};

function isValidAffId(id: string | undefined): id is string {
  return Boolean(id && !PLACEHOLDER_IDS.has(id));
}

/** Apply (or refresh) iHerb affiliate rcode on any product URL */
export function withIherbAffiliate(url: string): string {
  if (!url) return url;
  try {
    const u = new URL(url);
    const affId = affiliateConfig.iherb.affiliateId;
    if (isValidAffId(affId)) {
      u.searchParams.set('rcode', affId);
    }
    return u.toString();
  } catch {
    return url;
  }
}

/** Apply Amazon associate tag; strip known placeholders if not configured */
export function withAmazonAffiliate(url: string): string {
  if (!url) return url;
  try {
    const u = new URL(url);
    const affId = affiliateConfig.amazon.affiliateId;
    if (isValidAffId(affId)) {
      u.searchParams.set('tag', affId);
    } else {
      const existing = u.searchParams.get('tag');
      if (existing && PLACEHOLDER_IDS.has(existing)) {
        u.searchParams.delete('tag');
      }
    }
    return u.toString();
  } catch {
    return url;
  }
}

/** @deprecated use withIherbAffiliate */
export function generateIherbLink(productPath: string): string {
  return withIherbAffiliate(productPath);
}

/** @deprecated use withAmazonAffiliate */
export function generateAmazonLink(productPath: string): string {
  return withAmazonAffiliate(productPath);
}
