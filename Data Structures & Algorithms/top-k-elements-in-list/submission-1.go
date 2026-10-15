func topKFrequent(nums []int, k int) []int {
	frequencyMap := map[int]int{}
	output := []int{}

	for _, number := range nums{
		if _, exist:= frequencyMap[number]; !exist{
			output = append(output, number)
		}
		
		frequencyMap[number]++
	}

	sort.Slice(output,  func(i, j int) bool{
		return frequencyMap[output[i]] > frequencyMap[output[j]]
	})

	return output[:k]
}
