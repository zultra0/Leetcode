function mergeAlternately(word1: string, word2: string): string {

  let mergedString = '';
  const x = word1.length;
  const y = word2.length;

  for (let i = 0; i < Math.max(x, y); i++) {
    if (i < x) mergedString += word1[i]; 
    if (i < y) mergedString += word2[i]; 
  }

  return mergedString;
};