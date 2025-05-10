---
layout: "post"
title: "Do Telecom Customers Churn?"
date: "2021-05-06 03:52:02 +0000"
author: "Vladimir"
wordpress_id: "269"
status: "publish"
categories:
  - "data-science"
---

<!-- Original WordPress Content (processed for shortcodes and media links) -->
<p>HOW TO READ THIS NOTEBOOK:<br />
This notebook has several sections:</p>
<p>Util functions that generate plots, train models and print out statistics<br />
Feel free to skip these ones unless you're interested in-deep on how results are generated<br />
NOTE: Some of the util functions I took from the open-source code (e.g. print ROC curve) and others are written by myself (and a mix of that)</p>
<p>Execution of functions<br />
The output of the analysis fitted with provided test dataset</p>
<p>My comments<br />
I used python docstring to write down my thoughts through the analysis and model engineering and to describe results<br />
I used # to comment on some code for readability</p>
<p>I split all processes into four sections: Explanatory Analysis, Data Processing, Model Engineering, Create Prediction.</p>

<!-- wp:code -->
<pre class="wp-block-code"><code>

In &#91;1]:
#install required packages if needed:
#!pip install ipykernel notebook numpy matplotlib pandas sklearn seaborn graphviz
#print versions 
import sys 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import sklearn

from sklearn.pipeline import Pipeline

from utils import *

from sklearn.dummy import DummyClassifier
from sklearn.tree import DecisionTreeClassifier , plot_tree
from xgboost import plot_tree as plot_tree_xgb
from sklearn.linear_model import LogisticRegression
import xgboost
from xgboost import XGBClassifier
#disable warnings for viz 
import warnings
warnings.filterwarnings('ignore')


print('Python: ',sys.version)
print('pandas: ',pd.__version__)
print('sklearn: ',sklearn.__version__)
print('xgboost: ',xgboost.__version__)





Python:  3.6.13 |Anaconda, Inc.| (default, Feb 23 2021, 21:15:04) 
&#91;GCC 7.3.0]
pandas:  1.1.5
sklearn:  0.24.1
xgboost:  1.4.1



In &#91;2]:
#provide path to the input data:
output_file_name = 'predictions_churn_dataset_test.csv'

#train dataset:
path_to_train = 'input/churn_dataset_train.csv'

#random seed
RANDOM_SEED = 42



In &#91;3]:
#1 - EXPLONATORY ANALYSIS 
#Read training dataset, print preview:
df_input = pd.read_csv(path_to_train)
print('Input shape:\n\n\n train:', df_input.shape)





Input shape:


 train: (3500, 20)



In &#91;4]:
print('Train dataset:')
df_input.head()

</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>Out[4]:</p>
<!-- /wp:paragraph -->

<!-- wp:table -->
<figure class="wp-block-table"><table><thead><tr><th>&nbsp;</th><th>state</th><th>account_length</th><th>area_code</th><th>international_plan</th><th>voice_mail_plan</th><th>number_vmail_messages</th><th>total_day_minutes</th><th>total_day_calls</th><th>total_day_charge</th><th>total_eve_minutes</th><th>total_eve_calls</th><th>total_eve_charge</th><th>total_night_minutes</th><th>total_night_calls</th><th>total_night_charge</th><th>total_intl_minutes</th><th>total_intl_calls</th><th>total_intl_charge</th><th>number_customer_service_calls</th><th>churn</th></tr></thead><tbody><tr><th>0</th><td>AR</td><td>173</td><td>area_code_408</td><td>no</td><td>no</td><td>0</td><td>154.6</td><td>81</td><td>26.28</td><td>147.3</td><td>100.0</td><td>12.52</td><td>132.9</td><td>99</td><td>5.98</td><td>6.9</td><td>5</td><td>1.86</td><td>0</td><td>no</td></tr><tr><th>1</th><td>ID</td><td>127</td><td>area_code_408</td><td>no</td><td>no</td><td>0</td><td>102.8</td><td>128</td><td>17.48</td><td>143.7</td><td>95.0</td><td>12.21</td><td>191.4</td><td>97</td><td>8.61</td><td>10.0</td><td>5</td><td>2.70</td><td>1</td><td>no</td></tr><tr><th>2</th><td>TX</td><td>91</td><td>area_code_415</td><td>no</td><td>no</td><td>0</td><td>251.5</td><td>57</td><td>42.76</td><td>179.1</td><td>113.0</td><td>15.22</td><td>163.2</td><td>72</td><td>7.34</td><td>6.6</td><td>3</td><td>1.78</td><td>1</td><td>no</td></tr><tr><th>3</th><td>ND</td><td>60</td><td>area_code_510</td><td>no</td><td>no</td><td>0</td><td>203.2</td><td>99</td><td>NaN</td><td>235.8</td><td>131.0</td><td>20.04</td><td>224.9</td><td>112</td><td>10.12</td><td>15.1</td><td>6</td><td>4.08</td><td>2</td><td>no</td></tr><tr><th>4</th><td>NV</td><td>83</td><td>area_code_510</td><td>no</td><td>yes</td><td>31</td><td>129.8</td><td>87</td><td>22.07</td><td>183.4</td><td>110.0</td><td>15.59</td><td>169.4</td><td>40</td><td>7.62</td><td>14.3</td><td>6</td><td>3.86</td><td>1</td><td>no</td></tr></tbody></table></figure>
<!-- /wp:table -->

<!-- wp:paragraph -->
<p>In&nbsp;[5]:</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code># We have provided with 19 input features and one target label

# 1.1 - Description analysis
# First thing I'll examine is a descriptive statistics:
#print statistics for each column:
for col in df_input.columns:
    print(df_input&#91;col].describe(),'\n','-'*60)





count     3500
unique      51
top         WV
freq       111
Name: state, dtype: object 
 ------------------------------------------------------------
count    3500.000000
mean      100.062286
std        40.126972
min         1.000000
25%        73.000000
50%       100.000000
75%       127.000000
max       232.000000
Name: account_length, dtype: float64 
 ------------------------------------------------------------
count              3500
unique                3
top       area_code_415
freq               1721
Name: area_code, dtype: object 
 ------------------------------------------------------------
count     3500
unique       2
top         no
freq      3183
Name: international_plan, dtype: object 
 ------------------------------------------------------------
count     3500
unique       2
top         no
freq      2579
Name: voice_mail_plan, dtype: object 
 ------------------------------------------------------------
count    3500.000000
mean        7.654857
std        13.430216
min         0.000000
25%         0.000000
50%         0.000000
75%        16.000000
max        52.000000
Name: number_vmail_messages, dtype: float64 
 ------------------------------------------------------------
count    3500.000000
mean      180.133229
std        53.946041
min         0.000000
25%       143.700000
50%       180.150000
75%       216.125000
max       351.500000
Name: total_day_minutes, dtype: float64 
 ------------------------------------------------------------
count    3500.000000
mean       99.821429
std        19.841249
min         0.000000
25%        87.000000
50%       100.000000
75%       113.000000
max       165.000000
Name: total_day_calls, dtype: float64 
 ------------------------------------------------------------
count    3216.000000
mean       30.643193
std         9.147634
min         0.000000
25%        24.480000
50%        30.620000
75%        36.725000
max        59.760000
Name: total_day_charge, dtype: float64 
 ------------------------------------------------------------
count    3500.000000
mean      200.012857
std        50.504487
min         0.000000
25%       165.800000
50%       199.900000
75%       233.900000
max       359.300000
Name: total_eve_minutes, dtype: float64 
 ------------------------------------------------------------
count    3269.000000
mean      100.109208
std        20.023304
min         0.000000
25%        87.000000
50%       100.000000
75%       114.000000
max       170.000000
Name: total_eve_calls, dtype: float64 
 ------------------------------------------------------------
count    3500.000000
mean       17.001297
std         4.292901
min         0.000000
25%        14.090000
50%        16.990000
75%        19.880000
max        30.540000
Name: total_eve_charge, dtype: float64 
 ------------------------------------------------------------
count    3500.000000
mean      199.786514
std        49.987834
min        43.700000
25%       167.000000
50%       199.300000
75%       233.325000
max       395.000000
Name: total_night_minutes, dtype: float64 
 ------------------------------------------------------------
count    3500.000000
mean       99.714286
std        20.025978
min        33.000000
25%        86.000000
50%        99.500000
75%       113.000000
max       175.000000
Name: total_night_calls, dtype: float64 
 ------------------------------------------------------------
count    3500.000000
mean        8.990494
std         2.249460
min         1.970000
25%         7.520000
50%         8.970000
75%        10.500000
max        17.770000
Name: total_night_charge, dtype: float64 
 ------------------------------------------------------------
count    3500.000000
mean       10.284829
std         2.777536
min         0.000000
25%         8.600000
50%        10.400000
75%        12.100000
max        20.000000
Name: total_intl_minutes, dtype: float64 
 ------------------------------------------------------------
count    3500.000000
mean        4.470286
std         2.497207
min         0.000000
25%         3.000000
50%         4.000000
75%         6.000000
max        20.000000
Name: total_intl_calls, dtype: float64 
 ------------------------------------------------------------
count    3500.000000
mean        2.777434
std         0.749906
min         0.000000
25%         2.320000
50%         2.810000
75%         3.270000
max         5.400000
Name: total_intl_charge, dtype: float64 
 ------------------------------------------------------------
count    3500.000000
mean        1.553714
std         1.315906
min         0.000000
25%         1.000000
50%         1.000000
75%         2.000000
max         9.000000
Name: number_customer_service_calls, dtype: float64 
 ------------------------------------------------------------
count     3500
unique       2
top         no
freq      3013
Name: churn, dtype: object 
 ------------------------------------------------------------</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>The following thing can be inferred from the descriptive statistics:</p>
<!-- /wp:paragraph -->

<!-- wp:list {"ordered":true} -->
<ol><!-- wp:list-item -->
<li><code>state</code>: 51 unique values. It looks like we have data from all US states.<br>It's a good sign since it reduces the risk of selection bias in our data.<br>Let's bring the distribution of observations by state:</li>
<!-- /wp:list-item --></ol>
<!-- /wp:list -->

<!-- wp:code -->
<pre class="wp-block-code"><code>In &#91;6]:
fig , ax = plt.subplots(figsize=(8,5))
df_input&#91;'state'].value_counts().plot.bar(ax=ax,label='obs in state')
ax.axhline(df_input&#91;'state'].value_counts().mean(),color='red',label='Mean')
ax.set(title='Figure 1: # of obs by state')
ax.legend();</code></pre>
<!-- /wp:code -->

<!-- wp:image {"align":"center","id":270,"sizeSlug":"full","linkDestination":"none"} -->
<figure class="wp-block-image aligncenter size-full"><img src="/media/2023/11/image.png" alt="" class="wp-image-270"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>From figure 1 we can see that WV, MN, AL are highly overrepresented in the dataset<br>whereas CA and AK are underrepresented.<br>To eliminate the Selection bias, we should clarify this distribution with data owners!</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>In &#91;7]:
churn_total = (df_input.replace({'yes':1,'no':0}).churn).value_counts()
fig , ax = plt.subplots(figsize=(5,5))

churn_total.plot.bar(ax=ax,label='# in class')
ax.set(title='Figure 2.1: Churn rate total')
ax.legend();</code></pre>
<!-- /wp:code -->

<!-- wp:image {"align":"center","id":271,"sizeSlug":"full","linkDestination":"none"} -->
<figure class="wp-block-image aligncenter size-full"><img src="/media/2023/11/image-1.png" alt="" class="wp-image-271"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>We can see that <code>no</code> class is clearly underrepresented in this dataset (~14%)<br>This will cause a challenge in creating a classification model since the accuracy score by itself<br>won't be that useful.<br>I assume the Recall measure is more suitable to capture the model's ability to identify churn customers.<br>I will also try resampling technics to balance classes in the training data.</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>In &#91;8]:
#Let's examine the churn rate by state
churn_by_state = (df_input.replace({'yes':1,'no':0})
                            .groupby('state')&#91;'churn']
                            .apply(lambda x: round(x.sum()/ x.count(),2))
                            .sort_values()
                    )
fig , ax = plt.subplots(figsize=(8,5))

churn_by_state.plot.bar(ax=ax,label='churn rate, pct')
ax.axhline(churn_by_state.mean(),color='red',label='Mean')
ax.set(title='Figure 2.1: Churn rate by state')
ax.legend();</code></pre>
<!-- /wp:code -->

<!-- wp:image {"id":272,"sizeSlug":"full","linkDestination":"none"} -->
<figure class="wp-block-image size-full"><img src="/media/2023/11/image-2.png" alt="" class="wp-image-272"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>Figure 2 shows an interesting story: The churn rate seems to be highly unbalanced state-by-state.<br>There might be several reasons for this including underrepresentation of the company in these regions,<br>high competitive pressure, or other factors. There's a story behind that, and it's a good follow-up<br>question to business people.<br>The decision we should make here whether or not to include the <code>state</code> variable in the model.<br>If it is included, the training score would certainly be higher since the geo-location itself can be a good predictor.<br>BUT with no information about the causes of this distribution, the model might fail to generalize new data.</p>
<!-- /wp:paragraph -->

<!-- wp:list {"ordered":true,"start":2} -->
<ol start="2"><!-- wp:list-item -->
<li><code>area_code</code>: there only three unique values. Why is that?<br>From the glance, this variable doesn't provide much information<br>and is the candidate for exclusion</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><code>account_length</code>: I assume this metric tends to trace how old the account in general.<br>The client with a two-digit account length is assumed to be `older than the one with three or more. Numerical representation of this metric might not be relevant.<br>I'll replace this metric to bins of # of digits: {2,3,...}</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>In all numerical variables min value is always zero (not below) which<br>also is a good sign.</li>
<!-- /wp:list-item --></ol>
<!-- /wp:list -->

<!-- wp:code -->
<pre class="wp-block-code"><code>In &#91;9]:
# I remove state variable in this exersice, to avoid geo bias in the model
# If 
vars_to_drop = &#91;'area_code'
                ,'state' 
                ]



In &#91;10]:
# Next one - sanity check of the provided dataset:
# define util function:

#print sanity check
sanity_stats = get_df_stats(df_input)
print(sanity_stats)





                          Feature  Unique_testues  \
8                total_day_charge            1608   
10                total_eve_calls             118   
11               total_eve_charge            1472   
18  number_customer_service_calls              10   
17              total_intl_charge             164   
16               total_intl_calls              21   
15             total_intl_minutes             164   
14             total_night_charge             946   
13              total_night_calls             124   
12            total_night_minutes            1636   
0                           state              51   
1                  account_length             212   
9               total_eve_minutes            1652   
7                 total_day_calls             118   
6               total_day_minutes            1670   
5           number_vmail_messages              46   
4                 voice_mail_plan               2   
3              international_plan               2   
2                       area_code               3   
19                          churn               2   

    Percentage of missing values  Number of missing values  \
8                       8.114286                       284   
10                      6.600000                       231   
11                      0.000000                         0   
18                      0.000000                         0   
17                      0.000000                         0   
16                      0.000000                         0   
15                      0.000000                         0   
14                      0.000000                         0   
13                      0.000000                         0   
12                      0.000000                         0   
0                       0.000000                         0   
1                       0.000000                         0   
9                       0.000000                         0   
7                       0.000000                         0   
6                       0.000000                         0   
5                       0.000000                         0   
4                       0.000000                         0   
3                       0.000000                         0   
2                       0.000000                         0   
19                      0.000000                         0   

    Percentage of values in the biggest category    dtype  
8                                       8.114286  float64  
10                                      6.600000  float64  
11                                      0.314286  float64  
18                                     35.628571    int64  
17                                      1.742857  float64  
16                                     19.371429    int64  
15                                      1.742857  float64  
14                                      0.485714  float64  
13                                      2.314286    int64  
12                                      0.314286  float64  
0                                       3.171429   object  
1                                       1.257143    int64  
9                                       0.228571  float64  
7                                       2.371429    int64  
6                                       0.257143  float64  
5                                      73.714286    int64  
4                                      73.685714   object  
3                                      90.942857   object  
2                                      49.171429   object  
19                                     86.085714   object  
</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>Following things can be observed:</p>
<!-- /wp:paragraph -->

<!-- wp:list {"ordered":true} -->
<ol><!-- wp:list-item -->
<li>Our target variable <code>churn</code> doesn't have missing values, which is good.</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>We observe significant number of missing values in <code>total_day_charge</code> and <code>total_eve_calls</code> variables<br>From the definition:- total_day_charge (total charge of day calls)<br>- total_eve_minutes (total minutes of evening calls)</li>
<!-- /wp:list-item --></ol>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>Another thing that I noticed is that <code>Percentage of missing values</code> == <code>Percentage of values in the biggest category.</code><br>I assume it's because of the missing values; let's validate:</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>In &#91;11]:
print('total_day_charge:\n',df_input&#91;'total_day_charge'].fillna(-9999).value_counts().iloc&#91;:3])
print('total_eve_calls:\n',df_input&#91;'total_eve_calls'].fillna(-9999).value_counts().iloc&#91;:3])





total_day_charge:
 -9999.00    284
 32.18        8
 26.18        7
Name: total_day_charge, dtype: int64
total_eve_calls:
 -9999.0    231
 105.0      74
 108.0      73
Name: total_eve_calls, dtype: int64



In &#91;12]:
print('Total pct of missing value: ',sanity_stats&#91;'Number of missing values'].sum() / df_input.shape&#91;0] )



Total pct of missing value:  0.14714285714285713</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>We have 14% of missing values which is significant enough, so we cannot just drop these rows because it'll have a noticeable impact on the performance of the model. Hence, these two features must be treated either:</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul><!-- wp:list-item -->
<li>Fill values using some method (mean, median, etc.)</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>Remove these two features completely from the model if the model shows a small significance level</li>
<!-- /wp:list-item --></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>If it possible, it's good to know when data was collected to prevent potential data leakage:<br>We don't want our model to be trained on the future data and be validated on the past.<br>Even though it's not that critical for this exercise, this type of data leakage can affect the production model dramatically.</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>n &#91;13]:
# 1.2 - Correlation Analysis
'''
In this dataset, most of the variables are related to some usage patterns:
num. of minutes, num. of calls, etc. I assume these variables could be highly correlated and hence hold redundant information.
'''
#plot correlation matrix for numerical features
num_varialbes = df_input.select_dtypes(include=np.number).columns.tolist()
numeric_features = df_input&#91;num_varialbes]
print('numerical variables: \n', num_varialbes)
fig = plt.figure(figsize=(8, 6))
plt.matshow(numeric_features.corr(), fignum=fig.number)
cb = plt.colorbar()
cb.ax.tick_params(labelsize=14)
plt.title('Figure 3: Correlation Matrix', fontsize=16);
print(numeric_features.corr().abs().applymap(lambda x : x>.85))





numerical variables: 
 &#91;'account_length', 'number_vmail_messages', 'total_day_minutes', 'total_day_calls', 'total_day_charge', 'total_eve_minutes', 'total_eve_calls', 'total_eve_charge', 'total_night_minutes', 'total_night_calls', 'total_night_charge', 'total_intl_minutes', 'total_intl_calls', 'total_intl_charge', 'number_customer_service_calls']
                               account_length  number_vmail_messages  \
account_length                           True                  False   
number_vmail_messages                   False                   True   
total_day_minutes                       False                  False   
total_day_calls                         False                  False   
total_day_charge                        False                  False   
total_eve_minutes                       False                  False   
total_eve_calls                         False                  False   
total_eve_charge                        False                  False   
total_night_minutes                     False                  False   
total_night_calls                       False                  False   
total_night_charge                      False                  False   
total_intl_minutes                      False                  False   
total_intl_calls                        False                  False   
total_intl_charge                       False                  False   
number_customer_service_calls           False                  False   

                               total_day_minutes  total_day_calls  \
account_length                             False            False   
number_vmail_messages                      False            False   
total_day_minutes                           True            False   
total_day_calls                            False             True   
total_day_charge                            True            False   
total_eve_minutes                          False            False   
total_eve_calls                            False            False   
total_eve_charge                           False            False   
total_night_minutes                        False            False   
total_night_calls                          False            False   
total_night_charge                         False            False   
total_intl_minutes                         False            False   
total_intl_calls                           False            False   
total_intl_charge                          False            False   
number_customer_service_calls              False            False   

                               total_day_charge  total_eve_minutes  \
account_length                            False              False   
number_vmail_messages                     False              False   
total_day_minutes                          True              False   
total_day_calls                           False              False   
total_day_charge                           True              False   
total_eve_minutes                         False               True   
total_eve_calls                           False              False   
total_eve_charge                          False               True   
total_night_minutes                       False              False   
total_night_calls                         False              False   
total_night_charge                        False              False   
total_intl_minutes                        False              False   
total_intl_calls                          False              False   
total_intl_charge                         False              False   
number_customer_service_calls             False              False   

                               total_eve_calls  total_eve_charge  \
account_length                           False             False   
number_vmail_messages                    False             False   
total_day_minutes                        False             False   
total_day_calls                          False             False   
total_day_charge                         False             False   
total_eve_minutes                        False              True   
total_eve_calls                           True             False   
total_eve_charge                         False              True   
total_night_minutes                      False             False   
total_night_calls                        False             False   
total_night_charge                       False             False   
total_intl_minutes                       False             False   
total_intl_calls                         False             False   
total_intl_charge                        False             False   
number_customer_service_calls            False             False   

                               total_night_minutes  total_night_calls  \
account_length                               False              False   
number_vmail_messages                        False              False   
total_day_minutes                            False              False   
total_day_calls                              False              False   
total_day_charge                             False              False   
total_eve_minutes                            False              False   
total_eve_calls                              False              False   
total_eve_charge                             False              False   
total_night_minutes                           True              False   
total_night_calls                            False               True   
total_night_charge                            True              False   
total_intl_minutes                           False              False   
total_intl_calls                             False              False   
total_intl_charge                            False              False   
number_customer_service_calls                False              False   

                               total_night_charge  total_intl_minutes  \
account_length                              False               False   
number_vmail_messages                       False               False   
total_day_minutes                           False               False   
total_day_calls                             False               False   
total_day_charge                            False               False   
total_eve_minutes                           False               False   
total_eve_calls                             False               False   
total_eve_charge                            False               False   
total_night_minutes                          True               False   
total_night_calls                           False               False   
total_night_charge                           True               False   
total_intl_minutes                          False                True   
total_intl_calls                            False               False   
total_intl_charge                           False                True   
number_customer_service_calls               False               False   

                               total_intl_calls  total_intl_charge  \
account_length                            False              False   
number_vmail_messages                     False              False   
total_day_minutes                         False              False   
total_day_calls                           False              False   
total_day_charge                          False              False   
total_eve_minutes                         False              False   
total_eve_calls                           False              False   
total_eve_charge                          False              False   
total_night_minutes                       False              False   
total_night_calls                         False              False   
total_night_charge                        False              False   
total_intl_minutes                        False               True   
total_intl_calls                           True              False   
total_intl_charge                         False               True   
number_customer_service_calls             False              False   

                               number_customer_service_calls  
account_length                                         False  
number_vmail_messages                                  False  
total_day_minutes                                      False  
total_day_calls                                        False  
total_day_charge                                       False  
total_eve_minutes                                      False  
total_eve_calls                                        False  
total_eve_charge                                       False  
total_night_minutes                                    False  
total_night_calls                                      False  
total_night_charge                                     False  
total_intl_minutes                                     False  
total_intl_calls                                       False  
total_intl_charge                                      False  
number_customer_service_calls                           True  </code></pre>
<!-- /wp:code -->

<!-- wp:image {"id":273,"width":"591px","height":"auto","sizeSlug":"full","linkDestination":"none"} -->
<figure class="wp-block-image size-full is-resized"><img src="/media/2023/11/image-3.png" alt="" class="wp-image-273" style="width:591px;height:auto"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>Nice plot, isn't it? :)<br>But examine these regular correlation spikes, I found out that <code>_time</code> and <code>_charge</code><br>variables are highly correlated, and hence, one of them can be excluded. I'd prefer to use <code>_time</code> variable as a feature.</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>In &#91;14]:
#extend the list of variables to exclude from the model
vars_to_drop.extend(&#91;c for c in numeric_features if '_charge' in c])



In &#91;15]:
def plot_dist(log,title ):
    fig = plt.figure(figsize=(8, 7))
    ax = fig.gca()
    for col in num_varialbes:
        if log:
            np.log1p(df_input&#91;col]).hist(ax=ax,alpha=.3,label=col)
        else:
            df_input&#91;col].hist(ax=ax,alpha=.3,label=col)

    ax.set(title=title)
    ax.legend()

plot_dist(log=False, title='Figure 4: Num. Vars Distribution (Linear)')

#Let's plot the distribution of the log-transformed variables 
plot_dist(log=True, title='Figure 5: Num. Vars Distribution (Log)')</code></pre>
<!-- /wp:code -->

<!-- wp:image {"id":274,"sizeSlug":"full","linkDestination":"none"} -->
<figure class="wp-block-image size-full"><img src="/media/2023/11/image-4.png" alt="" class="wp-image-274"/></figure>
<!-- /wp:image -->

<!-- wp:image {"id":275,"sizeSlug":"full","linkDestination":"none"} -->
<figure class="wp-block-image size-full"><img src="/media/2023/11/image-5.png" alt="" class="wp-image-275"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>We can see that most numerical features are distributed "more-or-less normally'<br>but have a different scale. This needs to be handled!<br>Since <code>*_total</code> variables tend to increase,in production through time,<br>these metrics will be accumulated and push the distribution in the axis right. To address this,<br>I'll use log(x+1) transform instead of norm() transform to address that.</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>In &#91;16]:
# A pair plot for `total_*` variables conditioned on three categorical variables:
cat_variable = &#91;'international_plan'
                ,'voice_mail_plan'
                ,'churn']
total_vars = &#91;c for c in df_input.columns if 'total_' in c and c not in vars_to_drop]
# total_vars = total_vars&#91;:4]
sample_size = 100
def plot_pairplot():
    for i , col in enumerate(cat_variable&#91;-1:]):
        
        #sample dataframe for performance/plot optimization
        df_toplot = (df_input&#91;total_vars+&#91;col]]
                    .sample(sample_size)
                    )
        #create pair plot
        ax = sns.pairplot(df_toplot,hue=col,size=1)
        fig = plt.gcf()
        fig.suptitle(f'Figure 4.{i}: Pair Plot {col}')
        # break
plot_pairplot()</code></pre>
<!-- /wp:code -->

<!-- wp:image {"id":277,"sizeSlug":"full","linkDestination":"none"} -->
<figure class="wp-block-image size-full"><img src="/media/2023/11/image-6.png" alt="" class="wp-image-277"/></figure>
<!-- /wp:image -->

<!-- wp:list -->
<ul><!-- wp:list-item -->
<li>Interesting that there is an order in churn distribution <code>total_day_minutes</code></li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>All other plots are distributed pretty much evenly.</li>
<!-- /wp:list-item --></ul>
<!-- /wp:list -->

<!-- wp:code -->
<pre class="wp-block-code"><code>In &#91;17]:
#2 - DATA PROCESSING



In &#91;18]:
target_label = 'churn'
#format featues names 
num_varialbes_touse = total_vars + &#91;c for c in df_input.columns if 'number_' in c]
cat_variables_touse = &#91;c for c in cat_variable if target_label not in c ]

#split featues-target variables 

df_totransform = df_input.copy()

#create the data pre-precessing object
processor = DataProcessing(num_varialbes_touse,cat_variables_touse
                            ,vars_to_drop=vars_to_drop,to_log1p=True)



X  , y = df_totransform.drop(target_label,axis=1) , df_totransform&#91;&#91;target_label]]

#Extract feature names for viz labeling 
X_ = processor.transform(X,y)
features_names = processor.features_names
columns_names = X.columns.tolist()



In &#91;19]:
#3 - MODEL ENGINERING</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>Before starting engineering any model I'll establish the baseline model and evaluation metrics:</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Baseline model:<br>- Most common classifier<br>- Random classifier</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Evaluation metric:<br>1 - Recall score: minimizing the type 2 error<br>2 - Accuracy score</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>In &#91;20]:
score_to_optimize = 'recall_score'

# 3.1 split input dataset on training- validation datasets - test dataset: Create Data Layer
dl = DataLayer(X,y,None,target_label,random_state=RANDOM_SEED)

def make_dummy_model(dl,strategy):
    '''
    A Wrapper for the dummy classifyer model
    '''
    print('*'*60,
        '\nDummy model with strategy: ', strategy)
    dummy_clf = Pipeline(steps = &#91;('processing', DataProcessing(num_varialbes_touse,cat_variables_touse
                                                    ,vars_to_drop=vars_to_drop,to_log1p=True,columns_names=columns_names))
                                ,('dummy_clf', DummyClassifier(strategy=strategy))
                                ])


    dummy_clf.fit(dl.X_train,dl.y_train)
    y_hat = dummy_clf.predict(dl.X_test)
    print_report(dl.y_test,y_hat)


# 3.2 Calculate scores on the baseline (null) models
make_dummy_model(dl,'most_frequent')

make_dummy_model(dl,'uniform')





************************************************************ 
Dummy model with strategy:  most_frequent
Confusion matrix:
     pred_neg  pred_pos
neg      1005         0
pos       150         0 
               precision    recall  f1-score   support

         0.0       0.87      1.00      0.93      1005
         1.0       0.00      0.00      0.00       150

    accuracy                           0.87      1155
   macro avg       0.44      0.50      0.47      1155
weighted avg       0.76      0.87      0.81      1155

************************************************************ 
Dummy model with strategy:  uniform
Confusion matrix:
     pred_neg  pred_pos
neg       498       507
pos        71        79 
               precision    recall  f1-score   support

         0.0       0.88      0.50      0.63      1005
         1.0       0.13      0.53      0.21       150

    accuracy                           0.50      1155
   macro avg       0.51      0.51      0.42      1155
weighted avg       0.78      0.50      0.58      1155

</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p><code>most_frequent</code> dummy model tells us what would be the model accuracy if we only use<br>the most frequent class: 87%.<br>This is our model's baseline accuracy. We can not accept an alternative model if it has a lower overall<br>accuracy.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><code>uniform</code> dummy model tells us the baseline <code>recall</code> score: 51%<br>We can not accept an alternative model if it has a lower <code>recall</code> performance than this.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>3.3 Create alternative models.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Model Selection reasoning:<br>I chose to test three models:</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>-Logistic Regression</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>-Decision Tree Classifier.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>-XGBoost</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Parameters selection justification:<br>I not want my model to overfit the data so the max depth should not be<br>very high ans well as min values for split and leaf should be at least</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>In &#91;21]:
'''
#3.3.1
'''

#model 1
#Create param greed for the model
param_RegClf = {'LogRegClf__C': &#91;0.01,0.1,1,10]
                ,'LogRegClf__penalty' : &#91;'l1','l2','elasticnet']
                }
#define the model pipeline
RegClf = Pipeline(steps = &#91;('Processing', DataProcessing(num_varialbes_touse,cat_variables_touse
                                                    ,vars_to_drop=vars_to_drop,to_log1p=True,columns_names=columns_names))
                                ,('LogRegClf', LogisticRegression()
                                        )
                                ])
#model 2
param_DT = {'DTClf__criterion': &#91;'gini','entropy']
                ,'DTClf__max_depth':range(3,6)
                ,'DTClf__min_samples_split': range(10,15)
                ,'DTClf__min_samples_leaf':range(10,15)
                }
#define the model pipeline
DTClf = Pipeline(steps = &#91;('Processing', DataProcessing(num_varialbes_touse,cat_variables_touse
                                                    ,vars_to_drop=vars_to_drop,to_log1p=True,columns_names=columns_names))
                                ,('DTClf', DecisionTreeClassifier()
                                        )
                                ])

#model 3
param_XGB =  {
        'XGBClf__max_depth': range(3,6),
        'XGBClf__min_child_weight':range(2,6),
        'XGBClf__subsample':&#91;1],
        'XGBClf__colsample_bytree':&#91;1],
        'XGBClf__eta':&#91;.3],
        'XGBClf__objective':&#91;'binary:logistic'],
        'XGBClf__n_jobs':&#91;-1],
        'XGBClf__verbosity': &#91;1],
        'XGBClf__eval_metrics': &#91;"auc"] }


#define the model pipeline
XGBClf = Pipeline(steps = &#91;('Processing', DataProcessing(num_varialbes_touse,cat_variables_touse
                                                    ,vars_to_drop=vars_to_drop,to_log1p=True,columns_names=columns_names))
                                ,('XGBClf', XGBClassifier()
                                        )
                                ])

#Train Loistic Regression 
best_model_LR = run_grid_search(dl,RegClf,param_RegClf,score_to_optimize,model_name='RegClf')

#Train Decigion Tree
best_model_DT = run_grid_search(dl,DTClf,param_DT,score_to_optimize,model_name='DTClf')

#Train XGBoost
best_model_XGB = run_grid_search(dl,XGBClf,param_XGB,score_to_optimize,model_name='XGBClf')





************************************************************ 
Starting training model: RegClf
Best params for recall_score : {'LogRegClf__C': 0.01, 'LogRegClf__penalty': 'l2'} 
Grid Search best scores:  0.7191226230581026 
Time took (sec.): 3
Confusion matrix:
     pred_neg  pred_pos
neg       663       342
pos        38       112 
               precision    recall  f1-score   support

         0.0       0.95      0.66      0.78      1005
         1.0       0.25      0.75      0.37       150

    accuracy                           0.67      1155
   macro avg       0.60      0.70      0.57      1155
weighted avg       0.86      0.67      0.72      1155

************************************************************ 
Starting training model: DTClf
Best params for recall_score : {'DTClf__criterion': 'entropy', 'DTClf__max_depth': 5, 'DTClf__min_samples_leaf': 14, 'DTClf__min_samples_split': 10} 
Grid Search best scores:  0.8521049461214109 
Time took (sec.): 26
Confusion matrix:
     pred_neg  pred_pos
neg       948        57
pos        35       115 
               precision    recall  f1-score   support

         0.0       0.96      0.94      0.95      1005
         1.0       0.67      0.77      0.71       150

    accuracy                           0.92      1155
   macro avg       0.82      0.85      0.83      1155
weighted avg       0.93      0.92      0.92      1155

************************************************************ 
Starting training model: XGBClf
&#91;19:36:16] WARNING: ../src/learner.cc:573: 
Parameters: { "eval_metrics" } might not be used.

  This may not be accurate due to some parameters are only used in language bindings but
  passed down to XGBoost core.  Or some parameters are not used but slip through this
  verification. Please open an issue if you find above cases.


&#91;19:36:16] WARNING: ../src/learner.cc:1095: Starting in XGBoost 1.3.0, the default evaluation metric used with the objective 'binary:logistic' was changed from 'error' to 'logloss'. Explicitly set eval_metric if you'd like to restore the old behavior.
Best params for recall_score : {'XGBClf__colsample_bytree': 1, 'XGBClf__eta': 0.3, 'XGBClf__eval_metrics': 'auc', 'XGBClf__max_depth': 5, 'XGBClf__min_child_weight': 2, 'XGBClf__n_jobs': -1, 'XGBClf__objective': 'binary:logistic', 'XGBClf__subsample': 1, 'XGBClf__verbosity': 1} 
Grid Search best scores:  0.9965151819378445 
Time took (sec.): 131
Confusion matrix:
     pred_neg  pred_pos
neg       983        22
pos        38       112 
               precision    recall  f1-score   support

         0.0       0.96      0.98      0.97      1005
         1.0       0.84      0.75      0.79       150

    accuracy                           0.95      1155
   macro avg       0.90      0.86      0.88      1155
weighted avg       0.95      0.95      0.95      1155

</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>3.3.2 Selecting Best Model Architechture</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Evaluation of the models' results:</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul><!-- wp:list-item -->
<li>XGB has a higher CV score across all models.</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>All models passed the baseline with <code>recall</code> metrics.</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>Logistic Regression has a lower accuracy score than the <code>most_frequent</code> null model,<br>hence it wouldn't be selected for future analysis.</li>
<!-- /wp:list-item --></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>Logistic Regression:<br>Recall = 75% (with overall accuracy 67%)</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Decision Tree scores:<br>Recall = 77% (with overall accuracy 92%)<br>Which is 24 percentage point higher than the uniform null model</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>XGB scores:<br>Recall = 75% (with overall accuracy 95%)<br>Which is 22 percentage point higher than the uniform null model</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>If to take into the account model performance using recall only, a Decision Tree would be<br>the favorite. BUT we see that it has done much weaker in <code>precision</code> score (67% vs 84% for XGB)<br>Even though the type 2 error has a higher cost: missing the customer who is about to churn,<br>Misclassification the significant number of users as an <code>about to churn</code> might create a wrong<br>perspective about the overall user experience and user satisfaction for the business.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Hence, I'm choosing the XGB model as the one to use.</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>In &#91;22]:
best_model = best_model_XGB
y_scores = best_model.predict_proba(dl.X_test)&#91;:, 1]
# importance = best_model&#91;'LogRegClf'].coef_&#91;0]
importance = best_model&#91;'XGBClf'].feature_importances_



In &#91;23]:
#3.3.3 Plot detailed report of for the best model
plot_reports(dl.y_test,y_scores,score_to_optimize,initial_threshold=0.5,title_prefix='Figure 6.')

0.9102023217247098
</code></pre>
<!-- /wp:code -->

<!-- wp:image {"id":278,"sizeSlug":"full","linkDestination":"none"} -->
<figure class="wp-block-image size-full"><img src="/media/2023/11/image-7.png" alt="" class="wp-image-278"/></figure>
<!-- /wp:image -->

<!-- wp:image {"id":279,"sizeSlug":"full","linkDestination":"none"} -->
<figure class="wp-block-image size-full"><img src="/media/2023/11/image-8.png" alt="" class="wp-image-279"/></figure>
<!-- /wp:image -->

<!-- wp:image {"id":280,"sizeSlug":"full","linkDestination":"none"} -->
<figure class="wp-block-image size-full"><img src="/media/2023/11/image-9.png" alt="" class="wp-image-280"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>Figures interpretation:</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul><!-- wp:list-item -->
<li>Figure 6.1<br>Shows the Precision-Recall tradeoff and current threshold position there.<br>We see that futher optimizing for recall won't improve <code>recall</code> much but would<br>dramatically reduce the <code>precision</code> score.</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>Figure 6.2<br>Shows both <code>precision</code> and <code>recall</code> scores as a function of the threshold.<br>It complements Figure 6.1 in the way that the threshold should not be further adjusted.</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>Figure 6.3<br>Is the ROC Curve. Which can be interpreted as "how much our classifier does better than a random guess."<br>We see that the ROC curve is very good!<br>Actually, it's migh be to-good-to-be-true! I should not exclude the possibility<br>that the model is overfitting due to some sort of data leakage.</li>
<!-- /wp:list-item --></ul>
<!-- /wp:list -->

<!-- wp:code -->
<pre class="wp-block-code"><code>In &#91;24]:
#3.3.4 Plot features importance
plot_feature_importance(importance,processor.features_names,'Figure 7: DTClf Feature Importance')





Feature: international_plan, Score: 0.2608954906463623
Feature: voice_mail_plan, Score: 0.12016084045171738
Feature: number_vmail_messages, Score: 0.04120601713657379
Feature: total_day_minutes, Score: 0.0951744019985199
Feature: total_day_calls, Score: 0.023855485022068024
Feature: total_eve_minutes, Score: 0.042013008147478104
Feature: total_eve_calls, Score: 0.030472613871097565
Feature: total_night_minutes, Score: 0.02721640281379223
Feature: total_night_calls, Score: 0.019038571044802666
Feature: total_intl_minutes, Score: 0.06032373756170273
Feature: total_intl_calls, Score: 0.05165725201368332
Feature: number_customer_service_calls, Score: 0.20180296897888184
Feature: account_length_bin, Score: 0.026183191686868668</code></pre>
<!-- /wp:code -->

<!-- wp:image {"id":281,"sizeSlug":"full","linkDestination":"none"} -->
<figure class="wp-block-image size-full"><img src="/media/2023/11/image-10.png" alt="" class="wp-image-281"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>Features importance interpretations:</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Top four important features in the model:</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul><!-- wp:list-item -->
<li><code>international_plan</code></li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><code>number_customer_service_calls</code></li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><code>voice_mail_plan</code></li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><code>total_day_minutes</code>.</li>
<!-- /wp:list-item --></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>The pattern is actually so strong that it's visible in the pair plots! (Section 1.2, figure 4.3)</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>I measured the importance of the feature by obtaining <code>feature_importances_</code> metric, which is calculated<br>by measuring how many splits were on that feature.</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>In &#91;25]:
#Plot Tree
fig, ax = plt.subplots(figsize=(8,8))
# plot_tree(best_model&#91;'DTClf']
#                 ,rounded = True
#                 ,filled = True
#                 ,feature_names=processor.features_names
#                 ,class_names=True
#                 ,fontsize=5
#                 ,ax=ax
#                 )

plot_tree_xgb(best_model&#91;'XGBClf'],ax=ax,features_names=processor.features_names)


ax.set(title = 'Figure 8: Decision Tree Plot');</code></pre>
<!-- /wp:code -->

<!-- wp:image {"id":282,"sizeSlug":"full","linkDestination":"none"} -->
<figure class="wp-block-image size-full"><img src="/media/2023/11/image-11.png" alt="" class="wp-image-282"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>Potential next steps:</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul><!-- wp:list-item -->
<li>Try out ensemble of different models and higher regularisation</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>Investigate potential data leakage in the Decision Tree model</li>
<!-- /wp:list-item --></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>Since this exercise has time constraints, I didn't test the following hypothesis:</p>
<!-- /wp:paragraph -->

<!-- wp:list {"ordered":true} -->
<ol><!-- wp:list-item -->
<li>Investigate the geo-biased model and compare results.</li>
<!-- /wp:list-item --></ol>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>The current model doesn't have <code>state</code> as a parameter, and I did it on purpose since the disbalance was found in the churn distribution by states (see Figure 2.1). It might be the temporal effect due to some business factors, so I don't want the model to judge based on where the user is from. The core assumption here<br>is that <code>churn</code> event should be related to behavioral factors.<br>But this hypothesis is need to be tested by compare performance of both: <code>geo-aweard</code> and <code>geo-not-awared</code> models as well as<br>by consulting with business users.</p>
<!-- /wp:paragraph -->

<!-- wp:list {"ordered":true,"start":2} -->
<ol start="2"><!-- wp:list-item -->
<li>Even though the Regression model didn't pass the null threshold, it might be fine-tuned for a better score. Then, two models can be used<br>as an ensemble to create a wotted prediction.</li>
<!-- /wp:list-item --></ol>
<!-- /wp:list -->