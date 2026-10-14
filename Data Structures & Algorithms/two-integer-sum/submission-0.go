func twoSum(nums []int, target int) []int {
    numsMap := map[int]int{}

	for index, number := range nums{
		difference := target - number
		
		if numsMapIndex, exist:= numsMap[difference]; exist{
			return getReturn(index, numsMapIndex)
		}

		numsMap[number] = index
	}

	return nil
}

func getReturn(index1 int, index2 int)[]int{
	if index1 > index2{
		return []int{index2, index1}
	}

	return []int{index1, index2}
}