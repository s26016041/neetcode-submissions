func hasDuplicate(nums []int) bool {
    repeatingNumbers := map[int]bool{}
    for _,number := range nums{
        if repeatingNumbers[number]{
            return true
        }
        repeatingNumbers[number] = true
    }

    return false
}
