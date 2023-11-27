# tuberculosis_detection
*An ML model for detecting Tuberculosis using CNN*

When hearing the word Tuberculosis one might think of an archaic disease beaten long ago by the efforts of humanity, but the idea that TB practically exists only in the pages of history books couldn't be farther from the truth. In 2022 a total of [1.3 ***million*** people died from TB](https://www.who.int/news-room/fact-sheets/detail/tuberculosis) (including 167 000 people with HIV). Worldwide, TB was the second leading infectious killer after COVID-19 (above HIV and AIDS). In 2019 it was [**the** most deadly infectious disease in the world](https://www.who.int/teams/global-tuberculosis-programme/tb-reports/global-tuberculosis-report-2021/disease-burden/mortality).

As with most diseases, low to middle income societies are hit the hardest, the reasons for which are multifaceted, ranging from insecure food sources to medical facilites being understaffed and not having sufficient access to life saving medicine. But a particularly big issue in fighting TB is diagnosing it, which is made difficult by its non-specific symptoms, slow onset, differing strains and high costs for good diagnostic equipment.


In this notebook I used a CNN to classify Normal and TB-infected lungs. I used the [data](https://www.kaggle.com/datasets/tawsifurrahman/tuberculosis-tb-chest-xray-dataset/data) provided by an [international team of researchers](https://ieeexplore.ieee.org/document/9224622) to fine tune the [EfficientNet](https://arxiv.org/abs/1905.11946) model to be able to distinguish TB infected and normal lungs with 99% success rate. Also my thanks to jaykumar1607 for his [brain tumour classification model](https://www.kaggle.com/code/jaykumar1607/brain-tumor-mri-classification-tensorflow-cnn) for having inspired this notebook.


I must add that the idea behind medical diagnostic software is not to replace doctors, but to supplement their work. It is my hope this type of technology will aide medical practitioners in giving more precise diagnoses and consequently better care to their patients.  
