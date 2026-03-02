import numpy as np

def cal_allocation(allocation_mat):
    """ Function to calculate the total allocated resources for the individaul resources of the allocation matrix. """
    rows=allocation_mat.shape[0]
    cols=allocation_mat.shape[1] 
    looping_cols=0
    individual_total_allocation=[]
    total=0
    while(looping_cols != cols):
        for i in range(rows):
            total+=allocation_mat[i][looping_cols]
        individual_total_allocation.append(total)
        total=0
        looping_cols+=1
    
    return (individual_total_allocation)

def check(allocation_mat,rem_need_mat):
    available_mat=list()
    available_mat=[0,1,4,1]
    no_of_process=allocation_mat.shape[0]
    visited=list()

    else_count=0
    while(else_count <= no_of_process) and  ( len(visited) != no_of_process) :
        for i in range(no_of_process):
            if(available_mat >= rem_need_mat[i]).all() and i not in visited:
                print(f"Entered the if block with else_count {else_count}")
                else_count=0
                visited.append(i)
                available_mat+=allocation_mat[i]
            else:
                print(f"Entered the else block with else_count {else_count}")
                else_count+=1
                
    status=True if (available_mat >= rem_need_mat[0]).all() else False
    print(status)

allocation_mat=np.array([[1,1,1,1],[2,0,1,0],[4,2,2,2],[0,2,1,1]])
rem_need_mat=np.array([[2,0,2,0],[0,4,2,2],[1,2,0,0],[0,1,3,0]])
resulting_mat=cal_allocation(allocation_mat)
#print(resulting_mat)
check(allocation_mat,rem_need_mat)
mat1=np.array([1,2,3,4])
mat2=np.array([1,2,3,5])
status=True if (mat1 >= mat2).all() else False
print(status)