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
