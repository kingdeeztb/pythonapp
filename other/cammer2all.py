#include<opencv2/opencv.hpp>
#include<iostream>
 
using namespace cv;
using namespace std;
 
//【画框】
void Draw_rectangle(Mat img,Point pt1, Point pt2)
{
	rectangle(img, pt1, pt2, Scalar(0, 255, 0), 2, 8, 0);
}
 
int main()
{
	Mat frame1, frame2,ROIImage1, ROIImage2,mask1,mask2,gray_Image1, gray_Image2;
	VideoCapture capture1(0);
	VideoCapture capture2(1);
	capture1.set(CV_CAP_PROP_FRAME_WIDTH, 320);
	capture1.set(CV_CAP_PROP_FRAME_HEIGHT, 240);
	capture2.set(CV_CAP_PROP_FRAME_WIDTH, 320);
	capture2.set(CV_CAP_PROP_FRAME_HEIGHT, 240);
	if (!capture1.isOpened())
	{
		cout << "Come on baby 1 !" << endl;
		return -1;
	}
	if (!capture2.isOpened())
	{
		cout << "Come on baby 2 !" << endl;
		return -1;
	}
	Mat frame3(240,640,CV_8UC3,Scalar(0,0,0));
	char temp_1[20];
	char temp_2[20];
	while (true)
	{
		capture1 >> frame1;
		capture2 >> frame2;
		Draw_rectangle(frame1, Point(0,0),Point(frame1.cols, frame1.rows));
		Draw_rectangle(frame2, Point(0, 0), Point(frame2.cols, frame2.rows));
		sprintf(temp_1, "capture1");
		putText(frame1, temp_1, Point(frame1.cols / 16, frame1.rows / 10), FONT_HERSHEY_SIMPLEX, 0.8, Scalar(255, 0, 255));
		sprintf(temp_2, "capture2");
		putText(frame2, temp_2, Point(frame2.cols / 16, frame2.rows / 10), FONT_HERSHEY_SIMPLEX, 0.8, Scalar(255, 0, 255));
		ROIImage1 = frame3(Rect(0,0,320,240));
		ROIImage2 = frame3(Rect(320, 0, 320, 240));
		//imshow("【ROIImage1】", ROIImage1);
		//imshow("【ROIImage2】", ROIImage2);
		cvtColor(frame1, gray_Image1,CV_RGB2GRAY);
		cvtColor(frame2, gray_Image2, CV_RGB2GRAY);
		mask1 = gray_Image1;
		mask2 = gray_Image2;
		frame1.copyTo(ROIImage1, mask1);
		frame2.copyTo(ROIImage2, mask2);
		imshow("【视频窗口一】", frame1);
		imshow("【视频窗口二】", frame2);
		imshow("【总窗口】", frame3);
		waitKey(1);
	}
 
	return 0;
}
