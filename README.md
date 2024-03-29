# Welfare_AI
## Machine Learning Methods for Lameness Identification in Dairy Cattle

This repository provides code for this bachelor thesis:

**Machine Learning Methods for Lameness Identification in Dairy Cattle**<br>
> [Yasmine Karoui](https://github.com/Yasminekaroui)<br>
**Abstract:** *Lameness, characterized by an anomalous gait in cows due to a dysfunction in their locomotive system, is a serious welfare issue for cows and farmers. Prompt lameness detection methods can prevent the development of acute lameness in cattle. In this study, we propose a deep learning framework to help identify lameness based on motion curves of different leg joints on the cow. The framework combines data augmentation and a convolutional neural network using an LeNet architecture. Performance assessed using cross validation showed promising prediction accuracies above 99\% and 91\% for 
validation and test sets, respectively. This also demonstrates the usefulness of data generation in cases where the data set is originally small in size and difficult to generate.*

This is the research pipeline of the study:
<p align="center">
  <img src="./images/overall_tech_route.png" alt="drawing" width="90%"/>
</p>

## Setting up an environment

This framework is built using Python 3.7 and relies on the PyTorch 1.4.0+. The following command installs all necessary packages:

```.bash
pip3 install -r requirements.txt
```

### Background: 
- Lameness can cause pain or physical/neurological trauma in affected dairy cows and reduce their milk productivity. It is the third leading cause of their culling after mastitis and infertility.

- Visual gait scoring is used to rank an animal's walking ability but traditional methods are costly, manually intensive, subjective and time-consuming, making them both susceptible to human error. They also cannot be scaled up as the size of the farm increases.

- Automatic lameness detection systems have been developed using various types of sensors (accelerometers, radars, RGB video and 3D imaging) and machine learning models like support vector machines, K- Nearest Neighbor and Long-Short-Term Memory cells with high accuracies (all above 94%).

- However, large and accessible datasets are necessary for developing such models, but unfortunately, these are still rare to come by or produce in the dairy farming sector.

### Objective: 
In this study, we investigate whether data augmentation can be used to mitigate the lack of available gait scoring data for a dairy farm, and we develop a CNN based on a modified LeNet architecture and a SVM as a baseline to test our hypothesis and classify lame and non- lame cows primarily using synthetic data.
The study is composed of 4 parts:
 
 1- Data Collection 
 
 2- Data Exploration and Preprocessing
 
 3- Data Augmentation
 
 4- Binary Classification Non-lame vs Lame cows



### Data Collection:
A set of 15 random Holstein cows (lame and non-lame) was selected for kinematic gait analysis. Reflective markers were placed on eight points on each side of the cow’s body (Fig. 2). (screenshot_ballerina.png , cow_markers.png)

<p float="left">
  <img src="./images/cow_markers.png"  width="45%"/>
  <img src="./images/screenshot_ballerina.png"  width="45%"/>
</p>

Videos of cows walking along a passageway were recorded and scored by a trained visual observer. A 3D biomechanical analysis program (Vicon Motus 10.0; CONTEMPLAS GmbH, Kempton, Germany) created a motion template, for each leg joint angle and each cow using the acquired video. Automatic tracking of the reflective markers in the X, Y and Z planes, as well as the rotational matrix R, was then carried out. This process was repeated three times across a span of 14 weeks.




### Data Exploration and Clustering
The data was first cleaned by removing outliers. 

<p float="left">
  <img src="./images/R-H.png"  width="45%"/>
  <img src="./images/X-FF.png"  width="45%"/>
</p>
 
 Unsupervised learning was then applied  to determine whether there existed characteristics in the data that could be used to create clusters that were independent of the cows' labels. Tests were done with and without cows that we deemed "problematic", to see if these particular cows would create additional bias in the groupings. Two clustering algorithms were explored The K-Means and the hirerachical clustering.
 The figure below shows an example of dendrograms. 

<p align="center">
  <img src="./images/S1.png" alt="drawing" width="60%"/>
</p>


### Data Augmentation
Additional synthetic data (up to 24 000 samples) was derived from the real cows (15 samples) by adding random variation with magnitudes of 1, 2, 5, 10, 15 and 20% to the original data and then smoothing with a median filter. 
A simulation of a synthetic cow  is shown in this video:
<p align="center">
  <img src="./videos/Joly0_Frames_30_to_201.gif" alt="drawing" width="70%"/>
</p>
The figure bellow shows the t-SNE visualization of the new created data
<p align="center">
  <img src="./images/tsne_report_gene_side2.png" alt="drawing" width="50%"/>
</p>

### Binary Classification Non-lame vs Lame cows
- A modified LeNet (Fig. 4) was created by adding 4 additional batch-normalization layers after max-pooling.
<p align="center">
  <img src="./images/LeNet_Original_Image.jpg" alt="drawing" width="80%"/>
</p>
- The model was trained using the generated and original samples. Each time sequence contained 192 values for each variable, corresponding to a total of 3 front and back steps. 

- The data set was balanced with 12000 (50%) lame and non- lame cow examples. 

- The model was tested using 13 examples of cows (6 lame, 7 non-lame) that were not generated nor included in the training process at the very end of the experiment.

- A SVM classifier was also trained and evaluated on the same data 

### Results 
Multiple CNN models were built based on the configuration mentioned in the previous section. During training, the models were evaluated following a 5-fold cross-validation framework using a Monte Carlo optimization approach.

  <table>
    <tr>
      <th>Variation (%)</th>
      <th>Accuracy (%)</th>
      <th>Precision (%)</th>
      <th>Recall (%)</th>
      <th>F1-score (%)</th>
    </tr>
    <tr>
      <td>1</td>
      <td>76.84</td>
      <td>78.60</td>
      <td>777.60</td>
      <td>76.40</td>
    </tr>
    <tr>
      <td>2</td>
      <td>83.80</td>
      <td>83.80</td>
      <td>83.60</td>
      <td>83.20</td>
    </tr>
    <tr>
      <td>5</td>
      <td>90.76</td>
      <td>92.20</td>
      <td>91.40</td>
      <td>90.60</td>
    </tr>
    <tr>
      <td>10</td>
      <td>81.54</td>
      <td>84.60</td>
      <td>82.40</td>
      <td>81.40</td>
    </tr>
    </tr>
    <tr>
      <td>15</td>
      <td>79.99</td>
      <td>84.60</td>
      <td>80.04</td>
      <td>80.02</td>
    </tr>

  </table>

<p align="left">
  <img src="./images/svm_eval.png" alt="drawing" width="50%"/>
</p>


