function strStr(haystack: string, needle: string): number {
    if(needle.length > haystack.length || needle.length === 0)
        return -1;
    let needleIndex: number = 0;
    let output: number = 0;
    for(let index=0; index<haystack.length; index++){
        if(haystack[index] === needle[needleIndex] && needleIndex < needle.length ){
            output = index - needleIndex;
            needleIndex++;
        }else{
            output = -1;
            index = index - needleIndex
            needleIndex = 0;
        }

        if(needle.length === needleIndex)
            break;
        else
            output = -1
    }
    return output;
};
