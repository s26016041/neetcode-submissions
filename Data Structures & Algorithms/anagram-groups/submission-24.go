var wordIndexMap map[string]int

func groupAnagrams(strs []string) [][]string {
	wordIndexMap = map[string]int{}
	output := [][]string{}

	for _, word := range strs{
		output = addOutput(word, output)
	}

	return output
}

func sortWord(word string)string{
	output := []rune(word)

	sort.Slice(output, func(i, j int)bool {
		return output[i] > output[j]
	})

	return string(output)
}

func addOutput(word string, output [][]string)[][]string{
	if index, exist :=  wordIndexMap[sortWord(word)]; exist{
		output[index] = append(output[index], word)
		return output
	}

	output = append(output, []string{word}) 
	wordIndexMap[sortWord(word)] = len(output)-1

	return output
}