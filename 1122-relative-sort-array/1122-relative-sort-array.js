/**
 * @param {number[]} arr1
 * @param {number[]} arr2
 * @return {number[]}
 */
var relativeSortArray = function(arr1, arr2) {
    const count = arr1.reduce((acc, v) => {
    acc[v] = (acc[v] || 0) + 1
    return acc
  }, [])

  const result = []
  arr2.forEach((num) => {
    while (count[num] > 0) {
      result.push(num)
      count[num] -= 1
    }
  })
  count.forEach((currentCount, key) => {
    const num = Number(key)
    for (let i = 0; i < currentCount; i++) {
      result.push(num)
    }
  })
  return result
};