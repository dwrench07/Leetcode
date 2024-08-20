function strStr(haystack: string, needle: string): number {
    let needleIndex: number = 0;
    let output: number = 0;
    for(let index=0; index < haystack.length; index++){
        if(haystack[index] == needle[needleIndex] && needleIndex < needle.length){
            needleIndex++;
            output = index - needleIndex;
        }else{
            needleIndex = 0;
            output = -1;
        }

        if(needle.length-1 == needleIndex)
            break;
    }
    return output;
};
