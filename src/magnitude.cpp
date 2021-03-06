// (参考元: https://cppsecrets.com/users/168511510411111711412197115105110104975764103109971051084699111109/C00-OpenCV-cvmagnitude.php)

#include<opencv2/opencv.hpp> 
#include<iostream>

using namespace cv;
using namespace std;

int main()
{
    double a[] = { 1,1,1,1,1,1, 1,1,1 };
    double b[] = { 1,2,1,1,1,1,1,1,1 };
    Mat m0(3, 3, CV_64FC1, a);
    Mat m1(3, 3, CV_64FC1, b);
    Mat dst;
    magnitude(m0, m1, dst);
    cout << m0 << "\n";
    cout << m1 << "\n";
    cout << dst << "\n";
    return 0;
}


