func isAnagram(s string, t string) bool {
	sCountMap := map[rune]int{}
	tCountMap := map[rune]int{}

	countString(s, sCountMap)
	countString(t, tCountMap)

	if len(sCountMap) != len(tCountMap){
		return false
	}

	for key, quantity := range sCountMap{
		if tCountMap[key] != quantity{
			return false
		}
	}

	return true
}

func countString(word string,countMap map[rune]int){
	for _, letter := range word{
		countMap[letter]++
	}
}