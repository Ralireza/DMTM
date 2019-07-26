**Frequency**
----------------

RFP: 1-4:2
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

 