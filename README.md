# Taylor_Approximation

The program for Mathematical Analysis to make approximation of sin (2x) ^ 3 using Taylor series.

## Preparing

The first step was to find the Taylor series for my function. In the following photo are shown my mathematical transformations to get the Taylor series of given function.

<img width="911" alt="Screenshot 2022-02-19 at 18 28 47" src="https://user-images.githubusercontent.com/54081501/154809560-6fe783ff-c2bf-447a-94b2-2237ad25d9ba.png">

Now, when we have the series, I created new venv and started working to implement the visualisator in code.

## Code

The whole program is realised in main, in which program calling functions, that are doing different computations. That is the list of all functions:

### calculation

The function that gets the result of my series after certain term that is chosen by user is calculated in function calculation!

<img width="687" alt="Screenshot 2022-02-19 at 17 07 03" src="https://user-images.githubusercontent.com/54081501/154806558-66346c8a-a81e-4aa3-a977-c7c4db782e60.png">

It is protected from OverflowError (too big numbers, that can't be computed by computer).

### factorial

The recursive function that gets factorial of n. It is cached, and in that way we don't have to calculate recursive result every time

### get_into_radius_pi

That is a function, that is reducing or increasing the input, till it is in the range of [-pi, pi]. As the sine is periodic, we can do this to make our result much more precise and to prevent too big values, that will crash our program.

### search_for_close

It is calculating the first term, after which the result of approximation is close enough to the sin (2x) ^ 3 that is found with the help of library math. In the program there are present checks after which the series differs from the result of math module by 10 ^ (-1), 10 ^ (-4), 10 ^ (-6). Output in the console looks like that:

<img width="505" alt="Screenshot 2022-02-19 at 17 36 58" src="https://user-images.githubusercontent.com/54081501/154807713-95cec578-6cf5-461a-9877-b1c717954db2.png">

### math_pi

Function to find the result of the desired sin with the help of library math. That is a very simple formula, that finds exact result.

<img width="189" alt="Screenshot 2022-02-19 at 17 37 53" src="https://user-images.githubusercontent.com/54081501/154807736-a5374fab-d95c-46d4-ac09-11560092eb43.png">

### visualise_difference

The function, that is visualising the values. It is using the library matplotlib. The user can change the scope of the graph (maximum values of the y axis, that is a result of approximation) and the amount of terms, that will be shown (x axis). Also, the user can see the red line, which shows the result of math library. In that way we can see the diference between the real value and the value of the aproximation after certain amount of terms.

### inputer

Function that is getting the input and lets to specify the result. Also, lets you to prevent crashing due to bad input or other bad outcomes.

## Working with the program

You start the program with python. You interact with it using interface. All required information is printed for you, so you just have to response to the instructions with suitable responses. Here is the example of the work.

<img width="818" alt="Screenshot 2022-02-19 at 17 56 19" src="https://user-images.githubusercontent.com/54081501/154808370-7b2b378d-1856-480f-a9b9-83cb21eda62a.png">

Also, here is the graph, that is created by that inputs:

<img width="636" alt="Screenshot 2022-02-19 at 17 57 13" src="https://user-images.githubusercontent.com/54081501/154808399-a6e60c8d-0872-4270-be1d-7a13434e6310.png">
