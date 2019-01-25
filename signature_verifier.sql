

CREATE DATABASE IF NOT EXISTS `signature_verifier` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;

USE `signature_verifier`;

CREATE TABLE IF NOT EXISTS `testing_features`(
  `ImageID` varchar(15) NOT NULL PRIMARY KEY,
  `AspectRatio` float(10,5) NOT NULL,
  `XCoG` float(10,5) NOT NULL,
  `YCoG` float(10,5) NOT NULL,
  `NormalisedArea` float(10,5) NOT NULL,
  `BaselineShift` float(10,5) NOT NULL,
  `Eccentricity` float(10,5) NOT NULL,
  `HuMoments` float(10,5) NOT NULL,
  `Corners` float(10,5) NOT NULL,
  `Contrast` float(10,5) NOT NULL,
  `Dissimilarity` float(10,5) NOT NULL,
  `Homogeneity` float(10,5) NOT NULL,
  `Energy` float(10,5) NOT NULL,
  `Correlation` float(10,5) NOT NULL,
  `ASM` float(10,5) NOT NULL,
  `Mean` float(10,5) NOT NULL,
  `Variances` float(10,5) NOT NULL,
  `Skewness` float(10,5) NOT NULL,
  `Kurtosis` float(10,5) NOT NULL,
  `Entropy` float(10,5) NOT NULL,
  `Haralick` float(10,5) NOT NULL,
  `AspectRatio_lbp` float(10,5) NOT NULL,
  `XCoG_lbp` float(10,5) NOT NULL,
  `YCoG_lbp` float(10,5) NOT NULL,
  `NormalisedArea_lbp` float(10,5) NOT NULL,
  `BaselineShift_lbp` float(10,5) NOT NULL,
  `Eccentricity_lbp` float(10,5) NOT NULL,
  `HuMoments_lbp` float(10,5) NOT NULL,
  `Corners_lbp` float(10,5) NOT NULL,
  `Contrast_lbp` float(10,5) NOT NULL,
  `Dissimilarity_lbp` float(10,5) NOT NULL,
  `Homogeneity_lbp` float(10,5) NOT NULL,
  `Energy_lbp` float(10,5) NOT NULL,
  `Correlation_lbp` float(10,5) NOT NULL,
  `ASM_lbp` float(10,5) NOT NULL,
  `Mean_lbp` float(10,5) NOT NULL,
  `Variances_lbp` float(10,5) NOT NULL,
  `Skewness_lbp` float(10,5) NOT NULL,
  `Kurtosis_lbp` float(10,5) NOT NULL,
  `Entropy_lbp` float(10,5) NOT NULL,
  `Haralick_lbp` float(10,5) NOT NULL
)  


CREATE TABLE IF NOT EXISTS `training_features` (
  `ImageID` varchar(15) NOT NULL PRIMARY KEY,
  `AspectRatio` float(10,5) NOT NULL,
  `XCoG` float(10,5) NOT NULL,
  `YCoG` float(10,5) NOT NULL,
  `NormalisedArea` float(10,5) NOT NULL,
  `BaselineShift` float(10,5) NOT NULL,
  `Eccentricity` float(10,5) NOT NULL,
  `HuMoments` float(10,5) NOT NULL,
  `Corners` float(10,5) NOT NULL,
  `Contrast` float(10,5) NOT NULL,
  `Dissimilarity` float(10,5) NOT NULL,
  `Homogeneity` float(10,5) NOT NULL,
  `Energy` float(10,5) NOT NULL,
  `Correlation` float(10,5) NOT NULL,
  `ASM` float(10,5) NOT NULL,
  `Mean` float(10,5) NOT NULL,
  `Variances` float(10,5) NOT NULL,
  `Skewness` float(10,5) NOT NULL,
  `Kurtosis` float(10,5) NOT NULL,
  `Entropy` float(10,5) NOT NULL,
  `Haralick` float(10,5) NOT NULL,
  `AspectRatio_lbp` float(10,5) NOT NULL,
  `XCoG_lbp` float(10,5) NOT NULL,
  `YCoG_lbp` float(10,5) NOT NULL,
  `NormalisedArea_lbp` float(10,5) NOT NULL,
  `BaselineShift_lbp` float(10,5) NOT NULL,
  `Eccentricity_lbp` float(10,5) NOT NULL,
  `HuMoments_lbp` float(10,5) NOT NULL,
  `Corners_lbp` float(10,5) NOT NULL,
  `Contrast_lbp` float(10,5) NOT NULL,
  `Dissimilarity_lbp` float(10,5) NOT NULL,
  `Homogeneity_lbp` float(10,5) NOT NULL,
  `Energy_lbp` float(10,5) NOT NULL,
  `Correlation_lbp` float(10,5) NOT NULL,
  `ASM_lbp` float(10,5) NOT NULL,
  `Mean_lbp` float(10,5) NOT NULL,
  `Variances_lbp` float(10,5) NOT NULL,
  `Skewness_lbp` float(10,5) NOT NULL,
  `Kurtosis_lbp` float(10,5) NOT NULL,
  `Entropy_lbp` float(10,5) NOT NULL,
  `Haralick_lbp` float(10,5) NOT NULL
)  


CREATE TABLE IF NOT EXISTS `training_classes`(
  `ImageID` varchar(15) NOT NULL PRIMARY KEY,
  `ActualClass` varchar(15) NOT NULL 
  )
  

CREATE TABLE IF NOT EXISTS `testing_classes`(
  `ImageID` varchar(15) NOT NULL PRIMARY KEY,
  `DecisionClass` varchar(15) NOT NULL 
  `ActualClass` varchar(15) NOT NULL 
  )  