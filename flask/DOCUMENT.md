**Frequency**
----------------

## RFP: 1-4:2
<div dir="rtl">
فراوانی نسبی و مطلق یک لیست از پرسش ها در یک لیست از پرسشنامه ها  محاسبه می کند.<br>
ورودی یک فایل اکسل حاوی دو ستون که ستون اول شامل همه پرسش هاست و ستون دوم شامل پرسش هایی است که فراوانی آنها را میخواهیم.<br>

</div>

-   **URL**

    /api/v1/frequency

-   **Method:**

    `POST`

-   **Data Params**

          {
              "data_file": [string]
          }

-   **Example**

        {
            "data_file": "/Users/a/project/DMTM/flask/files/sample2.csv"
        }

-   **Success Response:**

    -   **Code:** 200
    -   **Content:**

                {
                    "result_file": "/Users/a/project/DMTM/flask/dmtm_responses/1564146791027.json",
                    "results": [
                        {
                            "absolute": 1,
                            "id": 0,
                            "relative": 16.666666666666664
                        },
                        {
                            "absolute": 1,
                            "id": 1,
                            "relative": 16.666666666666664
                        },
                        {
                            "absolute": 1,
                            "id": 2,
                            "relative": 16.666666666666664
                        },
                        {
                            "absolute": 1,
                            "id": 3,
                            "relative": 16.666666666666664
                        },
                        {
                            "absolute": 2,
                            "id": 4,
                            "relative": 33.33333333333333
                        },
                        {
                            "absolute": 2,
                            "id": 5,
                            "relative": 33.33333333333333
                        }
                    ]
                }

-   **Error Response:**
    
        400
        
        
# descriptive feature
## RFP: 1-4:4
### minimum
<div dir="rtl">
مینیمم یک فایل اکسل که شامل یک ستون از اعداد است را محاسبه میکند.

</div>

-   **URL**

    /api/v1/desfeature/min

-   **Method:**

    `POST`

-   **Data Params**

          {
              "data_file": [string]
          }

-   **Example**

        {
            "data_file": "/Users/a/project/DMTM/flask/files/sample.csv"
        }

-   **Success Response:**

    -   **Code:** 200
    -   **Content:**

                {
                    "result_file": "/Users/a/project/DMTM/flask/dmtm_responses/1564146791027.json",
                    "results":
                    { 
                        "min": 0
                    }
                }

-   **Error Response:**
    
        400


## RFP: 1-4:4
###  maximum
<div dir="rtl">
ماکسیمم  فایل اکسل که شامل یک ستون از اعداد است را محاسبه میکند.

</div>

-   **URL**

    /api/v1/desfeature/max

-   **Method:**

    `POST`

-   **Data Params**

          {
              "data_file": [string]
          }

-   **Example**

        {
            "data_file": "/Users/a/project/DMTM/flask/files/sample.csv"
        }

-   **Success Response:**

    -   **Code:** 200
    -   **Content:**

                {
                    "result_file": "/Users/a/project/DMTM/flask/dmtm_responses/1564146791027.json",
                    "results":
                    { 
                        "max": 999
                    }
                }

-   **Error Response:**
    
        400


## RFP: 1-4:4
###  domainrange
<div dir="rtl">
دامنه تغییرات  فایل اکسل که شامل یک ستون از اعداد است را محاسبه میکند.

</div>

-   **URL**

    /api/v1/desfeature/domainrange

-   **Method:**

    `POST`

-   **Data Params**

          {
              "data_file": [string]
          }

-   **Example**

        {
            "data_file": "/Users/a/project/DMTM/flask/files/sample.csv"
        }

-   **Success Response:**

    -   **Code:** 200
    -   **Content:**

                {
                    "result_file": "/Users/a/project/DMTM/flask/dmtm_responses/1564146791027.json",
                    "results":
                    { 
                        "domainrange": 993
                    }
                }

-   **Error Response:**
    
        400


## RFP: 1-4:4
###  mean
<div dir="rtl">
معدل  فایل اکسل که شامل یک ستون از اعداد است را محاسبه میکند.

</div>

-   **URL**

    /api/v1/desfeature/mean

-   **Method:**

    `POST`

-   **Data Params**

          {
              "data_file": [string]
          }

-   **Example**

        {
            "data_file": "/Users/a/project/DMTM/flask/files/sample.csv"
        }

-   **Success Response:**

    -   **Code:** 200
    -   **Content:**

                {
                    "result_file": "/Users/a/project/DMTM/flask/dmtm_responses/1564146791027.json",
                    "results":
                    { 
                        "mean": 46.20
                    }
                }

-   **Error Response:**
    
        400


## RFP: 1-4:4
### trimmed mean
<div dir="rtl">
معدل پیراسته  فایل اکسل که شامل یک ستون از اعداد است را محاسبه میکند.<br> 
مقدار پارامتر باید بین 0 تا 0.5 بوده و باید در دیتای ارسالی باشد در غیر اینصورت کد ۴۰۰ بازگردانده میشود.
</div>

-   **URL**

    /api/v1/desfeature/tmean

-   **Method:**

    `POST`

-   **Data Params**

          {
              "data_file": [string],
              "parameters":{
                "limit":[float]
               }
          }

-   **Example**

        {
            "data_file": "/Users/a/project/DMTM/flask/files/sample.csv"
        }

-   **Success Response:**

    -   **Code:** 200
    -   **Content:**

                {
                    "result_file": "/Users/a/project/DMTM/flask/dmtm_responses/1564146791027.json",
                    "results":
                    { 
                        "tmean": 46.20
                    }
                }

-   **Error Response:**
    
        400


## RFP: 1-4:4
###  mode
<div dir="rtl">
مد  فایل اکسل که شامل یک ستون از اعداد است را محاسبه میکند.

</div>

-   **URL**

    /api/v1/desfeature/mode

-   **Method:**

    `POST`

-   **Data Params**

          {
              "data_file": [string]
          }

-   **Example**

        {
            "data_file": "/Users/a/project/DMTM/flask/files/sample.csv"
        }

-   **Success Response:**

    -   **Code:** 200
    -   **Content:**

                {
                    "result_file": "/Users/a/project/DMTM/flask/dmtm_responses/1564146791027.json",
                    "results":
                    { 
                        "mode": 97
                    }
                }

-   **Error Response:**
    
        400


## RFP: 1-4:4
###  median
<div dir="rtl">
میانه  فایل اکسل که شامل یک ستون از اعداد است را محاسبه میکند.

</div>

-   **URL**

    /api/v1/desfeature/median

-   **Method:**

    `POST`

-   **Data Params**

          {
              "data_file": [string]
          }

-   **Example**

        {
            "data_file": "/Users/a/project/DMTM/flask/files/sample.csv"
        }

-   **Success Response:**

    -   **Code:** 200
    -   **Content:**

                {
                    "result_file": "/Users/a/project/DMTM/flask/dmtm_responses/1564146791027.json",
                    "results":
                    { 
                        "median": 33
                    }
                }

-   **Error Response:**
    
        400



## RFP: 1-4:4
### weighted median

<div dir="rtl">
میانه وزن دار  فایل اکسل که شامل یک ستون از اعداد است را محاسبه میکند.

</div>

-   **URL**

    /api/v1/desfeature/wmedian

-   **Method:**

    `POST`

-   **Data Params**

          {
              "data_file": [string]
              
          }

-   **Example**

        {
            "data_file": "/Users/a/project/DMTM/flask/files/sample.csv"
        }

-   **Success Response:**

    -   **Code:** 200
    -   **Content:**

                {
                    "result_file": "/Users/a/project/DMTM/flask/dmtm_responses/1564146791027.json",
                    "results":
                    { 
                        "wmedian": 15
                    }
                }

-   **Error Response:**
    
        400
        
## RFP: 1-4:4
### variance

<div dir="rtl">
واریانس  فایل اکسل که شامل یک ستون از اعداد است را محاسبه میکند.

</div>

-   **URL**

    /api/v1/desfeature/variance

-   **Method:**

    `POST`

-   **Data Params**

          {
              "data_file": [string]
              
          }

-   **Example**

        {
            "data_file": "/Users/a/project/DMTM/flask/files/sample.csv"
        }

-   **Success Response:**

    -   **Code:** 200
    -   **Content:**

                {
                    "result_file": "/Users/a/project/DMTM/flask/dmtm_responses/1564146791027.json",
                    "results":
                    { 
                        "variance": 15
                    }
                }

-   **Error Response:**
    
        400
        
        
## RFP: 1-4:4
### deviation

<div dir="rtl">
انحراف معیار  فایل اکسل که شامل یک ستون از اعداد است را محاسبه میکند.

</div>

-   **URL**

    /api/v1/desfeature/deviation

-   **Method:**

    `POST`

-   **Data Params**

          {
              "data_file": [string]
              
          }

-   **Example**

        {
            "data_file": "/Users/a/project/DMTM/flask/files/sample.csv"
        }

-   **Success Response:**

    -   **Code:** 200
    -   **Content:**

                {
                    "result_file": "/Users/a/project/DMTM/flask/dmtm_responses/1564146791027.json",
                    "results":
                    { 
                        "deviation": 44 
                    }
                }

-   **Error Response:**
    
        400
## RFP: 1-4:4
### deviation

<div dir="rtl">
انحراف معیار  فایل اکسل که شامل یک ستون از اعداد است را محاسبه میکند.

</div>

-   **URL**

    /api/v1/desfeature/deviation

-   **Method:**

    `POST`

-   **Data Params**

          {
              "data_file": [string]
              
          }

-   **Example**

        {
            "data_file": "/Users/a/project/DMTM/flask/files/sample.csv"
        }

-   **Success Response:**

    -   **Code:** 200
    -   **Content:**

                {
                    "result_file": "/Users/a/project/DMTM/flask/dmtm_responses/1564146791027.json",
                    "results":
                    { 
                        "deviation": 44 
                    }
                }

-   **Error Response:**
    
        400
        
## RFP: 1-4:4
### quantile

<div dir="rtl">
چندک   فایل اکسل که شامل یک ستون از اعداد است را محاسبه میکند که پارامتر آن عددی بین ۰ و ۱ میباشد.

</div>

-   **URL**

    /api/v1/desfeature/quantile

-   **Method:**

    `POST`

-   **Data Params**

          {
              "data_file": [string],
              "parameters":{
              "q":[float]  // 0 < q < 1
              }
              
          }

-   **Example**

        {
            "data_file": "/Users/a/project/DMTM/flask/files/sample.csv"
        }

-   **Success Response:**

    -   **Code:** 200
    -   **Content:**

                {
                    "result_file": "/Users/a/project/DMTM/flask/dmtm_responses/1564146791027.json",
                    "results":
                    { 
                        "quantile": 44 
                    }
                }

-   **Error Response:**
    
        400
        
        
## RFP: 1-4:4
### skewness

<div dir="rtl">
چولگی   فایل اکسل که شامل یک ستون از اعداد است را محاسبه میکند .

</div>

-   **URL**

    /api/v1/desfeature/skewness

-   **Method:**

    `POST`

-   **Data Params**

          {
              "data_file": [string]
              
          }

-   **Example**

        {
            "data_file": "/Users/a/project/DMTM/flask/files/sample.csv"
        }

-   **Success Response:**

    -   **Code:** 200
    -   **Content:**

                {
                    "result_file": "/Users/a/project/DMTM/flask/dmtm_responses/1564146791027.json",
                    "results":
                    { 
                        "skewness": 0.81 
                    }
                }

-   **Error Response:**
    
        400
       
## RFP: 1-4:4
### kurtosis

<div dir="rtl">
کشیدگی   فایل اکسل که شامل یک ستون از اعداد است را محاسبه میکند .

</div>

-   **URL**

    /api/v1/desfeature/kurtosis

-   **Method:**

    `POST`

-   **Data Params**

          {
              "data_file": [string]
              
          }

-   **Example**

        {
            "data_file": "/Users/a/project/DMTM/flask/files/sample.csv"
        }

-   **Success Response:**

    -   **Code:** 200
    -   **Content:**

                {
                    "result_file": "/Users/a/project/DMTM/flask/dmtm_responses/1564146791027.json",
                    "results":
                    { 
                        "kurtosis": 11.71
                    }
                }

-   **Error Response:**
    
        400
        
        
## RFP: 1-4:6
### pearson

<div dir="rtl">
ضریب همبستگی پیرسون فایل اکسل که شامل دو ستون از اعداد است را محاسبه میکند .

</div>

-   **URL**

    /api/v1/coefficient/pearson

-   **Method:**

    `POST`

-   **Data Params**

          {
              "data_file": [string]
              
          }

-   **Example**

        {
            "data_file": "/Users/a/project/DMTM/flask/files/sample.csv"
        }

-   **Success Response:**

    -   **Code:** 200
    -   **Content:**

                {
                    "result_file": "/Users/a/project/DMTM/flask/dmtm_responses/1564146791027.json",
                    "results":
                    { 
                        "correlation": -0.13827040287560155,
                        "p_value": 1.1455692314984053e-65
                    }
                }

-   **Error Response:**
    
        400
       
## RFP: 1-4:6
### spearman

<div dir="rtl">
ضریب همبستگی اسپیرمن فایل اکسل که شامل دو ستون از اعداد است را محاسبه میکند .

</div>

-   **URL**

    /api/v1/coefficient/spearman

-   **Method:**

    `POST`

-   **Data Params**

          {
              "data_file": [string]
              
          }

-   **Example**

        {
            "data_file": "/Users/a/project/DMTM/flask/files/sample.csv"
        }

-   **Success Response:**

    -   **Code:** 200
    -   **Content:**

                {
                    "result_file": "/Users/a/project/DMTM/flask/dmtm_responses/1564146791027.json",
                    "results":
                    { 
                        "correlation": -0.13827040287560155,
                        "p_value": 1.1455692314984053e-65
                    }
                }

-   **Error Response:**
    
        400
        
        
## RFP: 1-4:6
### kendall

<div dir="rtl">
ضریب همبستگی تاوکندال فایل اکسل که شامل دو ستون از اعداد است را محاسبه میکند .

</div>

-   **URL**

    /api/v1/coefficient/kendall

-   **Method:**

    `POST`

-   **Data Params**

          {
              "data_file": [string]
              
          }

-   **Example**

        {
            "data_file": "/Users/a/project/DMTM/flask/files/sample.csv"
        }

-   **Success Response:**

    -   **Code:** 200
    -   **Content:**

                {
                    "result_file": "/Users/a/project/DMTM/flask/dmtm_responses/1564146791027.json",
                    "results":
                    { 
                        "correlation": -0.13827040287560155,
                        "p_value": 1.1455692314984053e-65
                    }
                }

-   **Error Response:**
    
        400
        
        
## RFP: 1-4:7
### cramers

<div dir="rtl">
ضریب همبستگی  کرامرز فایل اکسل که شامل دو ستون از اعداد است را محاسبه میکند .

</div>

-   **URL**

    /api/v1/coefficient/cramers

-   **Method:**

    `POST`

-   **Data Params**

          {
              "data_file": [string]
              
          }

-   **Example**

        {
            "data_file": "/Users/a/project/DMTM/flask/files/sample.csv"
        }

-   **Success Response:**

    -   **Code:** 200
    -   **Content:**

                {
                    "result_file": "/Users/a/project/DMTM/flask/dmtm_responses/1564146791027.json",
                    "results":
                    { 
                         "correlation": 0.23054475849398492
                    }
                }

-   **Error Response:**
    
        400

## RFP: 1-4:7
### tavafogh

<div dir="rtl">
ضریب همبستگی توافقی فایل اکسل که شامل دو ستون از اعداد است را محاسبه میکند .

</div>

-   **URL**

    /api/v1/coefficient/tavafogh

-   **Method:**

    `POST`

-   **Data Params**

          {
              "data_file": [string]
              
          }

-   **Example**

        {
            "data_file": "/Users/a/project/DMTM/flask/files/sample.csv"
        }

-   **Success Response:**

    -   **Code:** 200
    -   **Content:**

                {
                    "result_file": "/Users/a/project/DMTM/flask/dmtm_responses/1564146791027.json",
                    "results":
                    { 
                         "correlation": -0.02430
                    }
                }

-   **Error Response:**
    
        400
        
        
## RFP: 1-4:7
### somersd

<div dir="rtl">
ضریب همبستگی دی سامرز فایل اکسل که شامل دو ستون از اعداد است را محاسبه میکند .

</div>

-   **URL**

    /api/v1/coefficient/somersd

-   **Method:**

    `POST`

-   **Data Params**

          {
              "data_file": [string]
              
          }

-   **Example**

        {
            "data_file": "/Users/a/project/DMTM/flask/files/sample.csv"
        }

-   **Success Response:**

    -   **Code:** 200
    -   **Content:**

                {
                    "result_file": "/Users/a/project/DMTM/flask/dmtm_responses/1564146791027.json",
                    "results":
                    { 
                         "correlation": -0.177522
                    }
                }

-   **Error Response:**
    
        400
       
## RFP: 1-4:8
### eta omga

<div dir="rtl">
ضریب اتا و امگا فایل اکسل که شامل دو ستون از اعداد است را محاسبه میکند .

</div>

-   **URL**

    /api/v1/coefficient/etaomg

-   **Method:**

    `POST`

-   **Data Params**

          {
              "data_file": [string]
              
          }

-   **Example**

        {
            "data_file": "/Users/a/project/DMTM/flask/files/sample.csv"
        }

-   **Success Response:**

    -   **Code:** 200
    -   **Content:**

                {
                    "result_file": "/Users/a/project/DMTM/flask/dmtm_responses/1564146791027.json",
                    "results":
                    { 
                         "eta": 15.29170365615457,
                         "omg": 15.311781551099397
                    }
                }

-   **Error Response:**
    
        400  
        
             
## RFP: 1-4:16.3
### cronbachalpha

<div dir="rtl">
ضریب پایایی فایل اکسل که شامل دو ستون از اعداد است را محاسبه میکند .

</div>

-   **URL**

    /api/v1/coefficient/cronbachalpha

-   **Method:**

    `POST`

-   **Data Params**

          {
              "data_file": [string]
              
          }

-   **Example**

        {
            "data_file": "/Users/a/project/DMTM/flask/files/sample.csv"
        }

-   **Success Response:**

    -   **Code:** 200
    -   **Content:**

                {
                    "result_file": "/Users/a/project/DMTM/flask/dmtm_responses/1564146791027.json",
                    "results":
                    { 
                         "correlation": -0.018211507452472908
                    }
                }

-   **Error Response:**
    
        400



## RFP: 1-4:16.4
### point biserial

<div dir="rtl">
ضریب همبستگی دورشته ای نقطه ای فایل اکسل که شامل دو ستون از اعداد است را محاسبه میکند .

</div>

-   **URL**

    /api/v1/coefficient/pbiserial

-   **Method:**

    `POST`

-   **Data Params**

          {
              "data_file": [string]
              
          }

-   **Example**

        {
            "data_file": "/Users/a/project/DMTM/flask/files/sample.csv"
        }

-   **Success Response:**

    -   **Code:** 200
    -   **Content:**

                {
                    "result_file": "/Users/a/project/DMTM/flask/dmtm_responses/1564146791027.json",
                    "results":
                    { 
                         "pval": 1.1455692314984053e-65,
                         "rval": -0.13827040287560155
                    }
                }

-   **Error Response:**
    
        400




## RFP: 1-4:16.4
### matrix point biserial

<div dir="rtl">
ضریب همبستگی چندرشته ای نقطه ای فایل اکسل که شامل دو تا چند  ستون از اعداد است را محاسبه میکند .

</div>

-   **URL**

    /api/v1/coefficient/mpbiserial

-   **Method:**

    `POST`

-   **Data Params**

          {
              "data_file": [string]
              
          }

-   **Example**

        {
            "data_file": "/Users/a/project/DMTM/flask/files/sample.csv"
        }

-   **Success Response:**

    -   **Code:** 200
    -   **Content:**

                {
                    "result_file": "/Users/a/project/DMTM/flask/dmtm_responses/1564146791027.json",
                    "results":
                    { 
                        "mpbiserial": [
                            [
                                1.0,
                                -0.13827040287560155
                            ],
                            [
                                -0.13827040287560155,
                                0.9999999999999982
                            ]
                        ]
                    }
                }

-   **Error Response:**
    
        400


## RFP: 1-4:16.4
### biserial

<div dir="rtl">
ضریب همبستگی دورشته ای  فایل اکسل که شامل دو   ستون از اعداد است را محاسبه میکند .پارامتر های ورودی نیز مربوط به فرمول هستند و باید از کاربر گرفته شود و محدودیت خاصی ندارند.

</div>

-   **URL**

    /api/v1/coefficient/biserial

-   **Method:**

    `POST`

-   **Data Params**

          {
              "data_file": [string],
                "parameters":{
                    "p1":[float],
                    "p2":[float],
                    "y":[float]
                }
              
          }

-   **Example**

        {
            "data_file": "/Users/a/project/DMTM/flask/files/sample.csv",
            "parameters":{
                "p1":1,
                "p2":2,
                "y":4
            }   
        }

-   **Success Response:**

    -   **Code:** 200
    -   **Content:**

                {
                    "result_file": "/Users/a/project/DMTM/flask/dmtm_responses/1564146791027.json",
                    "results":
                    { 
                        "bserial": -0.04888596975536688
                    }
                }

-   **Error Response:**
    
        400




## RFP: 1-4:16.4
### matrix biserial

<div dir="rtl">
ضریب همبستگی چندرشته ای  فایل اکسل که شامل دو   ستون از اعداد است را محاسبه میکند .پارامتر های ورودی نیز مربوط به فرمول هستند و باید از کاربر گرفته شود و محدودیت خاصی ندارند.

</div>

-   **URL**

    /api/v1/coefficient/mbiserial

-   **Method:**

    `POST`

-   **Data Params**

          {
              "data_file": [string],
                "parameters":{
                    "p1":[float],
                    "p2":[float],
                    "y":[float]
                }
              
          }

-   **Example**

        {
            "data_file": "/Users/a/project/DMTM/flask/files/sample.csv",
            "parameters":{
                "p1":1,
                "p2":2,
                "y":4
            }   
        }

-   **Success Response:**

    -   **Code:** 200
    -   **Content:**

                {
                    "result_file": "/Users/a/project/DMTM/flask/dmtm_responses/1564146791027.json",
                    "results":
                    { 
                        "mbiserial": [
                            [
                                0.3535533905932738,
                                -0.04888596975536688
                            ],
                            [
                                -0.04888596975536688,
                                0.3535533905932732
                            ]
                        ]
                    }
                }

-   **Error Response:**
    
        400



