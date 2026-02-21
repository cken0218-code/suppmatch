// Affiliate Platform Configuration
export interface AffiliatePlatform {
  name: string;
  affiliateId: string;
  baseUrl: string;
  commission: string;
  color: string;
  logo: string;
}

export const affiliateConfig: Record<string, AffiliatePlatform> = {
  iherb: {
    name: 'iHerb',
    affiliateId: process.env.IHERB_AFF_ID || 'YOUR_AFF_ID',
    baseUrl: 'https://www.iherb.com',
    commission: '5-15%',
    color: '#40AF6E',
    logo: '🌿'
  },
  amazon: {
    name: 'Amazon',
    affiliateId: process.env.AMAZON_AFF_ID || 'YOUR_AFF_ID',
    baseUrl: 'https://www.amazon.com',
    commission: '3-10%',
    color: '#FF9900',
    logo: '📦'
  }
};

export function generateIherbLink(productPath: string): string {
  const affId = affiliateConfig.iherb.affiliateId;
  return productPath.includes('?') 
    ? `${productPath}&rcode=${affId}` 
    : `${productPath}/rcode=${affId}`;
}

export function generateAmazonLink(productPath: string): string {
  const affId = affiliateConfig.amazon.affiliateId;
  return productPath.includes('?') 
    ? `${productPath}&tag=${affId}` 
    : `${productPath}?tag=${affId}`;
}
