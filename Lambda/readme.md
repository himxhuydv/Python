# Lambda Function
**Defination:**
*Anonymous kind of function that don't have any name but they are an expression.*
*it's define using the lambda keyword.*
syntax:```lambda argument:expression ```
Lambda is actually a sub-part of the function.
So,let's just understand that with the example:
# Normal Function Example:
   ```def double(x):```
     ```  return=x*2``` 
     ```print(double(5))``` Output:10
**Lambda will also do the same but insingle expression,function have variable in single line.**
# Lambda Function Example:
```double=lamba x:x*2 ``` 
```print(double(5)) ```  Output:10
***both the output  are same nothing changes both are doing same job but the only difference is lambda  function is just cutting the extra line of code in just single line.the biggest drawback is that we cannot use lambda funtion for the complex logic building.we,only have to use function for that.***
*Some People say that Function is more readable type of form as compare to the lambda.*
*but if we need multiple function for simple logic we can use this kind of Lambda function.*

[lambda_code](file:///C:/Users/ashay/OneDrive/Desktop/SACRIFICES%20OF%20COMFORT/Python/Lambda/code.ipynb
)
**We can use multiple variable in the lambda function.**
``` avg=lambda x,y:(x+y)/2 ```
```print(avg(4,4))``output:4

### When you have to use the Lambda Function?
Answer:when you have to write only the single line of expresion

# MAIN USE OF THE FUNCTION COMES WHEN WE USE THE LAMBDA FUNCTION AS A ARUGMENT IN THE FUNCTION.
```Cube=lambda c:c*c*c ```
`def function_name(f,values):`
    ```return 6+f(values)```
``print(function_name(Cube,6))`` *here we are using the argument as the one of the lambda function.(cube)*
**So,this is what i am talking about we are using the lambda function as an argument**
