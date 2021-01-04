def partitionLabels(S):
    """
    Given a string, the algorithm creates a max cardinality partiions of the string, 
    such that no characters appear in more than one partition.

    Time: O(n)
    Space: O(n)
    such
    """
    #store the largest end index of each character
    end = {}
    for i in range(len(S)-1, -1, -1):
        if(S[i] not in end):
            end[S[i]] = i
    partitions = []
    prev = 0
    index = -1
    for i in range(len(S)):
        #keep track of the max index
        index = max(end[S[i]], index)
        #found the max index of a charracter in a partition
        if(i >= index):
            #add the length to the partitions
            partitions.append(index-prev+1)
            #update index and index of previous partition
            index = -1
            prev = i+1
    return partitions