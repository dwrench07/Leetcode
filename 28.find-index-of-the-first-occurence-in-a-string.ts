function strStr(haystack: string, needle: string): number {
    let needleIndex: number = 0;
    let output: number = 0;
    for(let index=0; index < haystack.length; index++){
        if(haystack[index] === needle[needleIndex] && needleIndex < needle.length){
            output = index - needleIndex;
            needleIndex++;
        }else{
            needleIndex = 0;
            output = -1;
        }

        if(needle.length === needleIndex)
            break;
        else
        	output = -1;
    }
    return output;
};
