#include <opencv2/opencv.hpp>

using namespace cv;

void mat_infos(Mat img)
{
  std::cout << "rows:" << img.rows << std::endl;
  std::cout << "cols:" << img.cols << std::endl;
  std::cout << "type:" << img.type() << std::endl;
  return;
}

int main(int argc, const char * argv[])
{
    Mat img = imread( "images/template.jpg" );

    double resize = 0.05;
    Mat dst = Mat::ones(img.rows*resize, img.cols*resize, CV_8U);

    cv::resize(img, dst, dst.size(), cv::INTER_CUBIC);
    std::cout << dst << std::endl;

    mat_infos(dst);
    imshow("img", dst );

    Mat gx,gy;
    Sobel(dst, gx, CV_16S, 1, 0, 3, 10);
    Sobel(dst, gy, CV_16S, 0, 1, 3, 10);
    mat_infos(gx);
    imshow("gx", gx );
    imshow("gy", gy );
    std::cout << gx << std::endl;

    //絶対値を計算し符号なし8-bitへ変換(参考: https://stackoverflow.com/questions/17815690/compute-absolute-values-of-x-and-y-derivatives-using-opencv)
    //convertScaleAbs(gx, gx);
    //convertScaleAbs(gy, gy);

    /*
    for (int i=0;i<img.cols;i++)
    {
      for (int j=0;j<img.rows;j++)
      {
        std::cout << i << "," << j << ":" << (int)img.at<Vec3b>(j,i)[0] << std::endl;
      }
    }
    */


    waitKey(0);

    return 0;
}
