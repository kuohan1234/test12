print ("Hello world")


#generator 的好處 是減少mom的使用量 使數據處理更快
def myGen(nums):
       # print("generator execution")
        for i in nums:
            yield (i*i)

# yield () ; same as return but release the memory occupy
myG =myGen([1,2,3,4,5])
# myGen = [i*i for x in[1,2,3,4,5]] 相同效果
x=next(myG)

print(x) # x= 1
x=next(myG)
print(x) # x=2*2
x=next(myG)
print(x) # x=3*3