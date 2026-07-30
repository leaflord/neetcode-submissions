type DynamicArray struct {
	data    []int
	readAt  int
	writeAt int
}

func NewDynamicArray(capacity int) *DynamicArray {
	return &DynamicArray{
		data:    make([]int, capacity),
		readAt:  0,
		writeAt: 0,
	}
}

func (da *DynamicArray) Get(i int) int {
	return da.data[da.idx(i)]
}

func (da *DynamicArray) Set(i int, n int) {
	da.data[da.idx(i)] = n
}

func (da *DynamicArray) Pushback(n int) {
	if da.GetSize() == da.GetCapacity() {
		da.resize()
	}
	if da.writeAt == da.GetCapacity() {
		da.writeAt = 0

	}
	da.data[da.writeAt%da.GetCapacity()] = n
	da.writeAt = da.writeAt + 1
}

func (da *DynamicArray) Popback() int {
	da.writeAt = (da.writeAt - 1 + da.GetCapacity()) % da.GetCapacity()
	return da.data[da.writeAt]
}

func (da *DynamicArray) resize() {
	newdata := make([]int, da.GetCapacity()*2)
	for i := 0; i < da.GetCapacity(); i++ {
		newdata[i] = da.data[da.idx(i)]
	}
	da.data = newdata
}

func (da *DynamicArray) GetSize() (size int) {
	size = da.writeAt - da.readAt
	if size < 0 {
		size = da.GetCapacity() - size
	}
	return
}

func (da *DynamicArray) GetCapacity() int {
	return len(da.data)
}

func (da *DynamicArray) idx(i int) int {
	return (i + da.readAt) % da.GetCapacity()

}
