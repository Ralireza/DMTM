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



## RFP: 1-4:10
### chisquare test

<div dir="rtl">
آزمون آماری خی دو فایل اکسل که شامل یک ستون از اعداد است را محاسبه میکند .
</div>

-   **URL**

    /api/v1/test/chisquare

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
                       "chsq": 647854.0570438602,
                       "pval": 0.0
                    }
                }

-   **Error Response:**
    
        400


## RFP: 1-4:10
### t test

<div dir="rtl">
آزمون آماری تی  فایل اکسل که شامل یک ستون از اعداد است را محاسبه میکند .
</div>

-   **URL**

    /api/v1/test/t

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
                       "t": 118.667875473242,
                       "pval": 0.0
                    }
                }

-   **Error Response:**
    
        400

## RFP: 1-4:10
### f test

<div dir="rtl">
آزمون آماری اف  فایل اکسل که شامل تعدادی دلخواه ستون از اعداد است را محاسبه میکند .
</div>

-   **URL**

    /api/v1/test/anova

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
                       "fval": 118.667875473242,
                       "pval": 0.0
                    }
                }

-   **Error Response:**
    
        400


## RFP: 1-4:10
### kruskal test

<div dir="rtl">
آزمون آماری کروسکال والیس  فایل اکسل که شامل تعدادی دلخواه ستون از اعداد است را محاسبه میکند .
</div>

-   **URL**

    /api/v1/test/kruskal

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
                       "krusk": 5458.714,
                       "pval": 0.0
                    }
                }

-   **Error Response:**
    
        400


## RFP: 1-4:10
### mannwhitney test

<div dir="rtl">
آزمون آماری من ویتنی  فایل اکسل که شامل دو ستون از اعداد است را محاسبه میکند .
</div>

-   **URL**

    /api/v1/test/manwhit

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
                       "manwhit": 59213220,
                       "pval": 0.0
                    }
                }

-   **Error Response:**
    
        400


## RFP: 1-4:10
### median test

<div dir="rtl">
آزمون آماری میانه والیس  فایل اکسل که شامل تعدادی دلخواه ستون از اعداد است را محاسبه میکند .
</div>

-   **URL**

    /api/v1/test/median

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
                       "median": 6512.815904,
                       "pval": 0.0
                    }
                }

-   **Error Response:**
    
        400



## RFP: 1-4:17
### normal test

<div dir="rtl">
آزمون آماری نرمال  فایل اکسل که شامل یک  ستون از اعداد است را محاسبه میکند .
</div>

-   **URL**

    /api/v1/test/normal

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
                       "normal": 4196.5560711,
                       "pval": 0.0
                    }
                }

-   **Error Response:**
    
        400


## RFP: 1-4:16.2
### korvit test

<div dir="rtl">
آزمون آماری کرویت  فایل اکسل که شامل تعدادی دلخواه  ستون از اعداد است را محاسبه میکند .
</div>

-   **URL**

    /api/v1/test/korvit

-   **Method:**

    `POST`

-   **Data Params**

          {
              "data_file": [string]           
          }

-   **Example**

        {
            "data_file": "/Users/a/project/DMTM/flask/files/sample3.csv"
        }

-   **Success Response:**

    -   **Code:** 200
    -   **Content:**

                {
                    "result_file": "/Users/a/project/DMTM/flask/dmtm_responses/1564146791027.json",
                    "results":
                    { 
                       "chival": 2.5464201254704735,
                       "pval": 0.06998370525047698
                    }
                }

-   **Error Response:**
    
        400


## RFP: 1-4:16.2
### kmo test

<div dir="rtl">
آزمون آماری kmo  فایل اکسل که شامل تعدادی دلخواه  ستون از اعداد است را محاسبه میکند .
</div>

-   **URL**

    /api/v1/test/kmo

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
                       "kmo": 0.4999670
                    }
                }

-   **Error Response:**
    
        400



## RFP: 1-4:16.2
### exploratory factor analyzer 

<div dir="rtl">
تحلیل عاملی اکتشافی  فایل اکسل که شامل تعدادی دلخواه  ستون از اعداد است را محاسبه میکند .
</div>

-   **URL**

    /api/v1/test/efa

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
                        "communalities": [
                            0.1382704086130894,
                            0.13827040843962485
                        ],
                        "loadings": [
                            0.37184728826187724,
                            5.315428264315876e-05,
                            -0.3718472880286302,
                            5.315428267650063e-05
                        ]
                    }
                }

-   **Error Response:**
    
        400



## RFP: 1-4:16.2
### confirmatory factor analyzer 

<div dir="rtl">
تحلیل عاملی تحلیلی  فایل اکسل که شامل تعدادی دلخواه  ستون از اعداد است را محاسبه میکند .
</div>

-   **URL**

    /api/v1/test/cfa

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
                        "loadings": [
                            2.935052899285504,
                            2.9350529129473486,
                            6.879576271701552,
                            6.879576271701552
                        ],
                        "trans": [
                            -0.18217654836379416,
                            -0.18217654767021113,
                            -0.18938895522051263,
                            -0.1893889544994705,
                            -0.4608506760520243,
                            -0.4608506742974724,
                            0.5072963640000627,
                            0.5072963620686827,
                            -0.04283948451967909,
                            -0.042839484356580484,
                            0.36795930015594763,
                            0.36795929875505207
                        ],
                        "varcovs": [
                            1.0,
                            0.1502351511622517,
                            0.1502351511622517,
                            1.0
                        ]
                    }
                }

-   **Error Response:**
    
        400



## RFP: 1-4: 18
### kmeans clustering 

<div dir="rtl">
خوشه بندی به روش کمینز است که فایل اکسل که دارای تعداد ستون دلخواه که هر ستون یک بعد از داده ها میباشد .<br>
ncluster <br>
مشخص میکند که چه تعداد خوشه میخواهیم.<br>
isfast<br>
این پارامتر که یا صفر است و یا یک مشخص میکند که الگوریتم fastkmeans<br>
هست یا خیر .
</div>

-   **URL**

    /api/v1/clustering/kmeans

-   **Method:**

    `POST`

-   **Data Params**

          {
              "data_file": [string],
              "parameters":{
              "isfast": 0 | 1 ,
              "ncluster":[int]
              }         
          }

-   **Example**

        {
            "data_file": "/Users/a/project/DMTM/flask/files/sample.csv",
            "parameters":{
              "isfast": 0,
              "ncluster":3
              }     
        }

-   **Success Response:**

    -   **Code:** 200
    -   **Content:**

                {
                    "result_file": "/Users/a/project/DMTM/flask/dmtm_responses/1564146791027.json"
                }

-   **Error Response:**
    
        400


## RFP: 1-4: 18
### dbscan clustering 

<div dir="rtl">
خوشه بندی به روش دی بی اسکن است که فایل اکسل که دارای تعداد ستون دلخواه که هر ستون یک بعد از داده ها میباشد .<br>


-   **URL**

    /api/v1/clustering/dbscan

-   **Method:**

    `POST`

-   **Data Params**

          {
              "data_file": [string],
              "parameters":{
                  "minsample":[int],
                  "eps":[int]
              }         
          }

-   **Example**

        {
            "data_file": "/Users/a/project/DMTM/flask/files/sample.csv",
            "parameters":{
                "minsample":4,
                "eps":3
                }   
        }

-   **Success Response:**

    -   **Code:** 200
    -   **Content:**

                {
                    "result_file": "/Users/a/project/DMTM/flask/dmtm_responses/1564146791027.json"
                }

-   **Error Response:**
    
        400



