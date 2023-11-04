# i collected data directly from responce section of network after submitting values 
#inspect element > go to network > submit the form > check the response send from server in network section there you will get all html content copy it and past it in python script

from bs4 import BeautifulSoup
import pandas as pd
count=0
def extract_data_from_html(html_content):
    global count
    soup = BeautifulSoup(html_content, 'html.parser')
    case=[]
    data = []
    rows = soup.find_all('tr')
    length=0
    for row in rows:
        columns = row.find_all('td')
        if length<8:
            if length==1:
                a = row.find_all('a')
                
                LIST=a[0].get_text().split('(English)')
               
                if len(LIST)<1:
                    judgment_date=LIST[0]
                    judgment_link =LIST[0] 
                    print(LIST[0],'HEloo')
                else:
                    judgment_link =LIST[-1] 
                    judgment_date=LIST[0]
                   
                                                                                                              
               
            case.append(columns)
            length+=1
        else:
            diary_number = case[0][2].get_text()
            case_number = case[1][1].get_text()
            petitioner_name = case[2][1].get_text()
            respondent_name =  case[3][1].get_text()
            petitioner_advocate =  case[4][1].get_text()
            respondent_advocate =  case[5][1].get_text()
            bench_name =    case[6][1].get_text()                                                                                                 
            judgment_by =    case[7][1].get_text()                                                                                                  
            
            data.append({
                
                'Diary Number': diary_number,
                'Case Number': case_number,
                'Petitioner Name': petitioner_name,
                'Respondent Name': respondent_name,
                'Petitioner Advocate': petitioner_advocate,
                'Respondent Advocate': respondent_advocate,
                'Bench': bench_name,
                'judgment_by':judgment_by,
                'Judgment Link': judgment_link,
                'Judgment Date': judgment_date
            })
            length=0
            case=[]

    return data



if __name__ == "__main__":
    # Sample HTML content (replace with your actual HTML content)
    html_content='''<table style='margin-left: auto;margin-right: auto;'>
            
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  1</td>
                    <td>Diary Number</td>
                                            <td>8 / 2009</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-000108-000108 / 2013</td>
                                        <td rowspan="5"><a href="/supremecourt/2009/8/8_2009_4_1501_40804_Judgement_09-Jan-2023.pdf" target="_blank"><a href=/supremecourt/2009/8/8_2009_4_1501_40804_Judgement_09-Jan-2023.pdf target="_blank">09-01-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2009/8/8_2009_4_1501_40804_Judgement_09-Jan-2023.pdf&dno=82009" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-01-09&dno=82009&filename=supremecourt/2009/8/8_2009_4_1501_40804_Judgement_09-Jan-2023.pdf target="_blank">2023 INSC 20 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>AMD INDUSTRIES LIMITED (EARLIER KNOWN AS M/S.ASHOKA METAL DECOR PVT.LTD)</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>COMMISSIONER OF TRADE TAX,LUCKNOW </td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td>BHAKTI VARDHAN SINGH</td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH, HON'BLE MR. JUSTICE KRISHNA MURARI</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  2</td>
                    <td>Diary Number</td>
                                            <td>84 / 2010</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-005393-005393 / 2010</td>
                                        <td rowspan="5"><a href="/supremecourt/2010/84/84_2010_14_1501_41414_Judgement_01-Feb-2023.pdf" target="_blank"><a href=/supremecourt/2010/84/84_2010_14_1501_41414_Judgement_01-Feb-2023.pdf target="_blank">01-02-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2010/84/84_2010_14_1501_41414_Judgement_01-Feb-2023.pdf&dno=842010" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-02-01&dno=842010&filename=supremecourt/2010/84/84_2010_14_1501_41414_Judgement_01-Feb-2023.pdf target="_blank">2023 INSC 92 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>M/S. GODREJ SARA LEE LTD.</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>THE EXCISE AND TAXATION OFFICER CUM ASSESSING AUTHORITY</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>RAJIV TYAGI</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td>KAMAL MOHAN GUPTA</td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE S. RAVINDRA BHAT, HON'BLE MR. JUSTICE DIPANKAR DATTA</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE DIPANKAR DATTA</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  3</td>
                    <td>Diary Number</td>
                                            <td>331 / 2009</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-000572-000573 / 2010</td>
                                        <td rowspan="5"><a href="/supremecourt/2009/331/331_2009_14_1501_42320_Judgement_27-Feb-2023.pdf" target="_blank"><a href=/supremecourt/2009/331/331_2009_14_1501_42320_Judgement_27-Feb-2023.pdf target="_blank">27-02-2023 <strong>(English)</strong><br><a href=/supremecourt_vernacular/2009/331/331_2009_14_1501_42320_Judgement_27-Feb-2023_HIN.pdf target="_blank">27-02-2023 <strong>(हिन्दी)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2009/331/331_2009_14_1501_42320_Judgement_27-Feb-2023.pdf&dno=3312009" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-02-27&dno=3312009&filename=supremecourt/2009/331/331_2009_14_1501_42320_Judgement_27-Feb-2023.pdf target="_blank">2023 INSC 172 <strong>(English)</strong><br><a href=/pdfdate/index1.php?dt=2023-02-27&dno=3312009&filename=supremecourt_vernacular/2009/331/331_2009_14_1501_42320_Judgement_27-Feb-2023_HIN.pdf target="_blank">2023 INSC 172 <strong>(हिन्दी)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>AMAN SEMI-CONDUCTORS (PVT.) LTD.</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>HARYANA STATE INDUST.DEV.CORP.LTD..</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>T. L. GARG</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td>RAVINDRA BANA</td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE S. RAVINDRA BHAT, HON'BLE MR. JUSTICE DIPANKAR DATTA</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE S. RAVINDRA BHAT</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  4</td>
                    <td>Diary Number</td>
                                            <td>449 / 2022</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-008957-008957 / 2022</td>
                                        <td rowspan="5"><a href="/supremecourt/2022/449/449_2022_4_1505_40734_Judgement_05-Jan-2023.pdf" target="_blank"><a href=/supremecourt/2022/449/449_2022_4_1505_40734_Judgement_05-Jan-2023.pdf target="_blank">05-01-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2022/449/449_2022_4_1505_40734_Judgement_05-Jan-2023.pdf&dno=4492022" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-01-05&dno=4492022&filename=supremecourt/2022/449/449_2022_4_1505_40734_Judgement_05-Jan-2023.pdf target="_blank">2023 INSC 15 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>M/S. SHEKHAR RESORTS LIMITED (UNIT HOTEL ORIENT TAJ)</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>UNION OF INDIA</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>CHARANYA LAKSHMIKUMARAN</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH, HON'BLE MR. JUSTICE C.T. RAVIKUMAR</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  5</td>
                    <td>Diary Number</td>
                                            <td>827 / 2013</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>W.P.(C) No.-000059-000059 / 2013</td>
                                        <td rowspan="5"><a href="/supremecourt/2013/827/827_2013_4_1507_41047_Judgement_13-Jan-2023.pdf" target="_blank"><a href=/supremecourt/2013/827/827_2013_4_1507_41047_Judgement_13-Jan-2023.pdf target="_blank">13-01-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2013/827/827_2013_4_1507_41047_Judgement_13-Jan-2023.pdf&dno=8272013" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-01-13&dno=8272013&filename=supremecourt/2013/827/827_2013_4_1507_41047_Judgement_13-Jan-2023.pdf target="_blank">2023 INSC 29 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>ASSOCIATION OF OLD SETTLERS OF SIKKIM</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>UNION OF INDIA</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>SENTHIL JAGADEESAN</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td>ARPUTHAM ARUNA AND CO</td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH, HON'BLE MRS. JUSTICE B.V. NAGARATHNA</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  6</td>
                    <td>Diary Number</td>
                                            <td>1847 / 2023</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>W.P.(Crl.) No.-000012 / 2023</td>
                                        <td rowspan="5"><a href="/supremecourt/2023/1847/1847_2023_15_1501_41710_Judgement_07-Feb-2023.pdf" target="_blank"><a href=/supremecourt/2023/1847/1847_2023_15_1501_41710_Judgement_07-Feb-2023.pdf target="_blank">07-02-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2023/1847/1847_2023_15_1501_41710_Judgement_07-Feb-2023.pdf&dno=18472023" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-02-07&dno=18472023&filename=supremecourt/2023/1847/1847_2023_15_1501_41710_Judgement_07-Feb-2023.pdf target="_blank">2023 INSC 101 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>RANA AYYUB</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>DIRECTORATE OF ENFORCEMENT</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>AAKARSH KAMRA</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE V. RAMASUBRAMANIAN, HON'BLE MR. JUSTICE PANKAJ MITHAL</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE V. RAMASUBRAMANIAN</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  7</td>
                    <td>Diary Number</td>
                                            <td>2236 / 2022</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-000073-000073 / 2023</td>
                                        <td rowspan="5"><a href="/supremecourt/2022/2236/2236_2022_4_1503_41103_Judgement_19-Jan-2023.pdf" target="_blank"><a href=/supremecourt/2022/2236/2236_2022_4_1503_41103_Judgement_19-Jan-2023.pdf target="_blank">19-01-2023 <strong>(English)</strong><br><a href=/supremecourt_vernacular/2022/2236/2236_2022_4_1503_41103_Judgement_19-Jan-2023_KAN.pdf target="_blank">19-01-2023 <strong>(ಕನ್ನಡ)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2022/2236/2236_2022_4_1503_41103_Judgement_19-Jan-2023.pdf&dno=22362022" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-01-19&dno=22362022&filename=supremecourt/2022/2236/2236_2022_4_1503_41103_Judgement_19-Jan-2023.pdf target="_blank">2023 INSC 57 <strong>(English)</strong><br><a href=/pdfdate/index1.php?dt=2023-01-19&dno=22362022&filename=supremecourt_vernacular/2022/2236/2236_2022_4_1503_41103_Judgement_19-Jan-2023_KAN.pdf target="_blank">2023 INSC 57 <strong>(ಕನ್ನಡ)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>M/S ALPINE HOUSING DEVELOPMENT CORPORATION PRIVATE LIMITED</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>ASHOK S DHARIWAL</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>M. C. DHINGRA</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH, HON'BLE MS. JUSTICE HIMA KOHLI</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  8</td>
                    <td>Diary Number</td>
                                            <td>2411 / 2017</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>Crl.A. No.-000466-000466 / 2017</td>
                                        <td rowspan="5"><a href="/supremecourt/2017/2411/2411_2017_4_1501_41103_Judgement_19-Jan-2023.pdf" target="_blank"><a href=/supremecourt/2017/2411/2411_2017_4_1501_41103_Judgement_19-Jan-2023.pdf target="_blank">19-01-2023 <strong>(English)</strong><br><a href=/supremecourt_vernacular/2017/2411/2411_2017_4_1501_41103_Judgement_19-Jan-2023_TAM.pdf target="_blank">19-01-2023 <strong>(தமிழ்)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2017/2411/2411_2017_4_1501_41103_Judgement_19-Jan-2023.pdf&dno=24112017" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-01-19&dno=24112017&filename=supremecourt/2017/2411/2411_2017_4_1501_41103_Judgement_19-Jan-2023.pdf target="_blank">2023 INSC 54 <strong>(English)</strong><br><a href=/pdfdate/index1.php?dt=2023-01-19&dno=24112017&filename=supremecourt_vernacular/2017/2411/2411_2017_4_1501_41103_Judgement_19-Jan-2023_TAM.pdf target="_blank">2023 INSC 54 <strong>(தமிழ்)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>JOHN ANTHONISAMY @ JOHN</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>STATE REP. BY THE INSPECTOR OF POLICE</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>RAKESH K. SHARMA</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH, HON'BLE MS. JUSTICE HIMA KOHLI</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  9</td>
                    <td>Diary Number</td>
                                            <td>2457 / 2022</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>W.P.(C) No.-000049 / 2022</td>
                                        <td rowspan="5"><a href="/supremecourt/2022/2457/2457_2022_5_1501_42140_Judgement_23-Feb-2023.pdf" target="_blank"><a href=/supremecourt/2022/2457/2457_2022_5_1501_42140_Judgement_23-Feb-2023.pdf target="_blank">23-02-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2022/2457/2457_2022_5_1501_42140_Judgement_23-Feb-2023.pdf&dno=24572022" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-02-23&dno=24572022&filename=supremecourt/2022/2457/2457_2022_5_1501_42140_Judgement_23-Feb-2023.pdf target="_blank">2023 INSC 155 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>C. YAMINI</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>THE HIGH COURT FOR THE STATE OF ANDHRA PRADESH AT AMARAVATHI</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>ARUNA GUPTA</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE AJAY RASTOGI, HON'BLE MS. JUSTICE BELA M. TRIVEDI</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE AJAY RASTOGI</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  10</td>
                    <td>Diary Number</td>
                                            <td>2475 / 2016</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-001497-001497 / 2023</td>
                                        <td rowspan="5"><a href="/supremecourt/2016/2475/2475_2016_13_1501_42415_Judgement_28-Feb-2023.pdf" target="_blank"><a href=/supremecourt/2016/2475/2475_2016_13_1501_42415_Judgement_28-Feb-2023.pdf target="_blank">28-02-2023 <strong>(English)</strong><br><a href=/supremecourt_vernacular/2016/2475/2475_2016_13_1501_42415_Judgement_28-Feb-2023_GUJ.pdf target="_blank">28-02-2023 <strong>(ગુજરાતી)</strong><br><a href=/supremecourt_vernacular/2016/2475/2475_2016_13_1501_42415_Judgement_28-Feb-2023_NAG.pdf target="_blank">28-02-2023 <strong>(Nagamese)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2016/2475/2475_2016_13_1501_42415_Judgement_28-Feb-2023.pdf&dno=24752016" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-02-28&dno=24752016&filename=supremecourt/2016/2475/2475_2016_13_1501_42415_Judgement_28-Feb-2023.pdf target="_blank">2023 INSC 176 <strong>(English)</strong><br><a href=/pdfdate/index1.php?dt=2023-02-28&dno=24752016&filename=supremecourt_vernacular/2016/2475/2475_2016_13_1501_42415_Judgement_28-Feb-2023_GUJ.pdf target="_blank">2023 INSC 176 <strong>(ગુજરાતી)</strong><br><a href=/pdfdate/index1.php?dt=2023-02-28&dno=24752016&filename=supremecourt_vernacular/2016/2475/2475_2016_13_1501_42415_Judgement_28-Feb-2023_NAG.pdf target="_blank">2023 INSC 176 <strong>(Nagamese)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>SHAH NEWAZ KHAN</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>THE STATE OF NAGALAND</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>DIKSHA RAI</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE S. RAVINDRA BHAT, HON'BLE MR. JUSTICE DIPANKAR DATTA</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE DIPANKAR DATTA</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  11</td>
                    <td>Diary Number</td>
                                            <td>2483 / 2022</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-000413-000413 / 2023</td>
                                        <td rowspan="5"><a href="/supremecourt/2022/2483/2483_2022_4_1503_41935_Judgement_17-Feb-2023.pdf" target="_blank"><a href=/supremecourt/2022/2483/2483_2022_4_1503_41935_Judgement_17-Feb-2023.pdf target="_blank">17-02-2023 <strong>(English)</strong><br><a href=/supremecourt_vernacular/2022/2483/2483_2022_4_1503_41935_Judgement_17-Feb-2023_KAN.pdf target="_blank">17-02-2023 <strong>(ಕನ್ನಡ)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2022/2483/2483_2022_4_1503_41935_Judgement_17-Feb-2023.pdf&dno=24832022" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-02-17&dno=24832022&filename=supremecourt/2022/2483/2483_2022_4_1503_41935_Judgement_17-Feb-2023.pdf target="_blank">2023 INSC 134 <strong>(English)</strong><br><a href=/pdfdate/index1.php?dt=2023-02-17&dno=24832022&filename=supremecourt_vernacular/2022/2483/2483_2022_4_1503_41935_Judgement_17-Feb-2023_KAN.pdf target="_blank">2023 INSC 134 <strong>(ಕನ್ನಡ)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>NATIONAL TECHNICAL RESEARCH ORGANIZATION</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>DIPTI DEODHARE</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>MUKESH KUMAR MARORIA</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH, HON'BLE MR. JUSTICE C.T. RAVIKUMAR</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  12</td>
                    <td>Diary Number</td>
                                            <td>2490 / 2023</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>SLP(C) No.-003006-003006 / 2023</td>
                                        <td rowspan="5"><a href="/supremecourt/2023/2490/2490_2023_1_18_41562_Judgement_07-Feb-2023.pdf" target="_blank"><a href=/supremecourt/2023/2490/2490_2023_1_18_41562_Judgement_07-Feb-2023.pdf target="_blank">07-02-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2023/2490/2490_2023_1_18_41562_Judgement_07-Feb-2023.pdf&dno=24902023" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-02-07&dno=24902023&filename=supremecourt/2023/2490/2490_2023_1_18_41562_Judgement_07-Feb-2023.pdf target="_blank">2023 INSC 102 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>ROPPEN TRANSPORTATION SERVICES PVT. LTD</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>UNION OF INDIA</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>B. VIJAYALAKSHMI MENON</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE THE CHIEF JUSTICE, HON'BLE MR. JUSTICE PAMIDIGHANTAM SRI NARASIMHA, HON'BLE MR. JUSTICE J.B. PARDIWALA</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE THE CHIEF JUSTICE</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  13</td>
                    <td>Diary Number</td>
                                            <td>2604 / 2022</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-003639-003639 / 2022</td>
                                        <td rowspan="5"><a href="/supremecourt/2022/2604/2604_2022_4_1504_41722_Judgement_09-Feb-2023.pdf" target="_blank"><a href=/supremecourt/2022/2604/2604_2022_4_1504_41722_Judgement_09-Feb-2023.pdf target="_blank">09-02-2023 <strong>(English)</strong><br><a href=/supremecourt_vernacular/2022/2604/2604_2022_4_1504_41722_Judgement_09-Feb-2023_HIN.pdf target="_blank">09-02-2023 <strong>(हिन्दी)</strong><br><a href=/supremecourt_vernacular/2022/2604/2604_2022_4_1504_41722_Judgement_09-Feb-2023_GUJ.pdf target="_blank">09-02-2023 <strong>(ગુજરાતી)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2022/2604/2604_2022_4_1504_41722_Judgement_09-Feb-2023.pdf&dno=26042022" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-02-09&dno=26042022&filename=supremecourt/2022/2604/2604_2022_4_1504_41722_Judgement_09-Feb-2023.pdf target="_blank">2023 INSC 109 <strong>(English)</strong><br><a href=/pdfdate/index1.php?dt=2023-02-09&dno=26042022&filename=supremecourt_vernacular/2022/2604/2604_2022_4_1504_41722_Judgement_09-Feb-2023_HIN.pdf target="_blank">2023 INSC 109 <strong>(हिन्दी)</strong><br><a href=/pdfdate/index1.php?dt=2023-02-09&dno=26042022&filename=supremecourt_vernacular/2022/2604/2604_2022_4_1504_41722_Judgement_09-Feb-2023_GUJ.pdf target="_blank">2023 INSC 109 <strong>(ગુજરાતી)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>STATE OF U.P.</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>PRIYANKA</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>SANJAY KUMAR TYAGI</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH, HON'BLE MR. JUSTICE C.T. RAVIKUMAR, HON'BLE MR. JUSTICE SANJAY KAROL</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  14</td>
                    <td>Diary Number</td>
                                            <td>2605 / 2019</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-001401 / 2019</td>
                                        <td rowspan="5"><a href="/supremecourt/2019/2605/2605_2019_14_1501_41407_Judgement_31-Jan-2023.pdf" target="_blank"><a href=/supremecourt/2019/2605/2605_2019_14_1501_41407_Judgement_31-Jan-2023.pdf target="_blank">31-01-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2019/2605/2605_2019_14_1501_41407_Judgement_31-Jan-2023.pdf&dno=26052019" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-01-31&dno=26052019&filename=supremecourt/2019/2605/2605_2019_14_1501_41407_Judgement_31-Jan-2023.pdf target="_blank">2023 INSC 89 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>K. L. SUNEJA</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>DR. (MRS.) MANJEET KAUR MONGA (D) THROUGH HER LR</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>MOHIT PAUL</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE S. RAVINDRA BHAT, HON'BLE MR. JUSTICE DIPANKAR DATTA</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE S. RAVINDRA BHAT</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  15</td>
                    <td>Diary Number</td>
                                            <td>2607 / 2022</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-001173-001173 / 2023</td>
                                        <td rowspan="5"><a href="/supremecourt/2022/2607/2607_2022_12_1501_41896_Judgement_15-Feb-2023.pdf" target="_blank"><a href=/supremecourt/2022/2607/2607_2022_12_1501_41896_Judgement_15-Feb-2023.pdf target="_blank">15-02-2023 <strong>(English)</strong><br><a href=/supremecourt_vernacular/2022/2607/2607_2022_12_1501_41896_Judgement_15-Feb-2023_HIN.pdf target="_blank">15-02-2023 <strong>(हिन्दी)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2022/2607/2607_2022_12_1501_41896_Judgement_15-Feb-2023.pdf&dno=26072022" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-02-15&dno=26072022&filename=supremecourt/2022/2607/2607_2022_12_1501_41896_Judgement_15-Feb-2023.pdf target="_blank">2023 INSC 129 <strong>(English)</strong><br><a href=/pdfdate/index1.php?dt=2023-02-15&dno=26072022&filename=supremecourt_vernacular/2022/2607/2607_2022_12_1501_41896_Judgement_15-Feb-2023_HIN.pdf target="_blank">2023 INSC 129 <strong>(हिन्दी)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>RAVINDER KUMAR GOEL</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>THE STATE OF HARYANA</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>ANSHUMAN ASHOK</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE A.S. BOPANNA, HON'BLE MR. JUSTICE J.B. PARDIWALA</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE A.S. BOPANNA</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  16</td>
                    <td>Diary Number</td>
                                            <td>2647 / 2010</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-003005-003005 / 2010</td>
                                        <td rowspan="5"><a href="/supremecourt/2010/2647/2647_2010_14_107_42417_Judgement_01-Mar-2023.pdf" target="_blank"><a href=/supremecourt/2010/2647/2647_2010_14_107_42417_Judgement_01-Mar-2023.pdf target="_blank">01-03-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2010/2647/2647_2010_14_107_42417_Judgement_01-Mar-2023.pdf&dno=26472010" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-03-01&dno=26472010&filename=supremecourt/2010/2647/2647_2010_14_107_42417_Judgement_01-Mar-2023.pdf target="_blank">2023 INSC 184 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>M/S DHARTI DREDGING AND INFRASTRUCTURE LTD.</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>COMMISSIONER  OF CUSTOMS AND CENTRAL EXCISE, GUNTUR</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>PRAVEEN KUMAR</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td>MUKESH KUMAR MARORIA</td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE S. RAVINDRA BHAT, HON'BLE MR. JUSTICE DIPANKAR DATTA</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE S. RAVINDRA BHAT</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  17</td>
                    <td>Diary Number</td>
                                            <td>2853 / 2016</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>SLP(C) No.-004428-004428 / 2016</td>
                                        <td rowspan="5"><a href="/supremecourt/2016/2853/2853_2016_4_1502_41935_Judgement_17-Feb-2023.pdf" target="_blank"><a href=/supremecourt/2016/2853/2853_2016_4_1502_41935_Judgement_17-Feb-2023.pdf target="_blank">17-02-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2016/2853/2853_2016_4_1502_41935_Judgement_17-Feb-2023.pdf&dno=28532016" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-02-17&dno=28532016&filename=supremecourt/2016/2853/2853_2016_4_1502_41935_Judgement_17-Feb-2023.pdf target="_blank">2023 INSC 131 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>S.M. PASHA </td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>STATE OF MAHARASHTRA .</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>BINDI GIRISH DAVE</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH, HON'BLE MR. JUSTICE C.T. RAVIKUMAR</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  18</td>
                    <td>Diary Number</td>
                                            <td>3007 / 2022</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>Crl.A. No.-000581-000581 / 2023</td>
                                        <td rowspan="5"><a href="/supremecourt/2022/3007/3007_2022_17_1502_42399_Judgement_01-Mar-2023.pdf" target="_blank"><a href=/supremecourt/2022/3007/3007_2022_17_1502_42399_Judgement_01-Mar-2023.pdf target="_blank">01-03-2023 <strong>(English)</strong><br><a href=/supremecourt_vernacular/2022/3007/3007_2022_17_1502_42399_Judgement_01-Mar-2023_PUN.pdf target="_blank">01-03-2023 <strong>(ਪੰਜਾਬੀ)</strong><br><a href=/supremecourt_vernacular/2022/3007/3007_2022_17_1502_42399_Judgement_01-Mar-2023_GUJ.pdf target="_blank">01-03-2023 <strong>(ગુજરાતી)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2022/3007/3007_2022_17_1502_42399_Judgement_01-Mar-2023.pdf&dno=30072022" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-03-01&dno=30072022&filename=supremecourt/2022/3007/3007_2022_17_1502_42399_Judgement_01-Mar-2023.pdf target="_blank">2023 INSC 188 <strong>(English)</strong><br><a href=/pdfdate/index1.php?dt=2023-03-01&dno=30072022&filename=supremecourt_vernacular/2022/3007/3007_2022_17_1502_42399_Judgement_01-Mar-2023_PUN.pdf target="_blank">2023 INSC 188 <strong>(ਪੰਜਾਬੀ)</strong><br><a href=/pdfdate/index1.php?dt=2023-03-01&dno=30072022&filename=supremecourt_vernacular/2022/3007/3007_2022_17_1502_42399_Judgement_01-Mar-2023_GUJ.pdf target="_blank">2023 INSC 188 <strong>(ગુજરાતી)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>SARABJIT KAUR</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>THE STATE OF PUNJAB</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>BANKEY BIHARI</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE ABHAY S. OKA, HON'BLE MR. JUSTICE RAJESH BINDAL</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE RAJESH BINDAL</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  19</td>
                    <td>Diary Number</td>
                                            <td>3247 / 2022</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>Crl.A. No.-000646-000648 / 2023</td>
                                        <td rowspan="5"><a href="/supremecourt/2022/3247/3247_2022_14_1501_42417_Judgement_01-Mar-2023.pdf" target="_blank"><a href=/supremecourt/2022/3247/3247_2022_14_1501_42417_Judgement_01-Mar-2023.pdf target="_blank">01-03-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2022/3247/3247_2022_14_1501_42417_Judgement_01-Mar-2023.pdf&dno=32472022" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-03-01&dno=32472022&filename=supremecourt/2022/3247/3247_2022_14_1501_42417_Judgement_01-Mar-2023.pdf target="_blank">2023 INSC 189 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>THE STATE OF CHHATTISGARH</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>AMAN KUMAR SINGH</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>GAUTAM NARAYAN</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE S. RAVINDRA BHAT, HON'BLE MR. JUSTICE DIPANKAR DATTA</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE DIPANKAR DATTA</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  20</td>
                    <td>Diary Number</td>
                                            <td>3256 / 2009</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>Crl.A. No.-001978-001978 / 2013</td>
                                        <td rowspan="5"><a href="/supremecourt/2009/3256/3256_2009_8_1501_41086_Judgement_18-Jan-2023.pdf" target="_blank"><a href=/supremecourt/2009/3256/3256_2009_8_1501_41086_Judgement_18-Jan-2023.pdf target="_blank">18-01-2023 <strong>(English)</strong><br><a href=/supremecourt_vernacular/2009/3256/3256_2009_8_1501_41086_Judgement_18-Jan-2023_TAM.pdf target="_blank">18-01-2023 <strong>(தமிழ்)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2009/3256/3256_2009_8_1501_41086_Judgement_18-Jan-2023.pdf&dno=32562009" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-01-18&dno=32562009&filename=supremecourt/2009/3256/3256_2009_8_1501_41086_Judgement_18-Jan-2023.pdf target="_blank">2023 INSC 51 <strong>(English)</strong><br><a href=/pdfdate/index1.php?dt=2023-01-18&dno=32562009&filename=supremecourt_vernacular/2009/3256/3256_2009_8_1501_41086_Judgement_18-Jan-2023_TAM.pdf target="_blank">2023 INSC 51 <strong>(தமிழ்)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>RAJARAM S/O SRIRAMULU NAIDU(SINCE DECEASED) THROUGH LRS.</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>MARUTHACHALAM (SINCE DECEASED)THROUGH LRS</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>NEHA SHARMA</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td>NIKHIL NAYYAR</td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE B.R. GAVAI, HON'BLE MR. JUSTICE VIKRAM NATH</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE B.R. GAVAI</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  21</td>
                    <td>Diary Number</td>
                                            <td>3324 / 2020</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>Crl.A. No.-000657-000664 / 2023</td>
                                        <td rowspan="5"><a href="/supremecourt/2020/3324/3324_2020_2_1501_42573_Judgement_01-Mar-2023.pdf" target="_blank"><a href=/supremecourt/2020/3324/3324_2020_2_1501_42573_Judgement_01-Mar-2023.pdf target="_blank">01-03-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2020/3324/3324_2020_2_1501_42573_Judgement_01-Mar-2023.pdf&dno=33242020" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-03-01&dno=33242020&filename=supremecourt/2020/3324/3324_2020_2_1501_42573_Judgement_01-Mar-2023.pdf target="_blank">2023 INSC 187 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>M/S. BLS INFRASTRUCTURE LTD.</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>M/S. RAJWANT SINGH</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>DEEPAK GOEL</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE SUDHANSHU DHULIA, HON'BLE MR. JUSTICE MANOJ MISRA</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE SANJAY KISHAN KAUL</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  22</td>
                    <td>Diary Number</td>
                                            <td>3379 / 2022</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-000366-000366 / 2023</td>
                                        <td rowspan="5"><a href="/supremecourt/2022/3379/3379_2022_4_1505_41177_Judgement_20-Jan-2023.pdf" target="_blank"><a href=/supremecourt/2022/3379/3379_2022_4_1505_41177_Judgement_20-Jan-2023.pdf target="_blank">20-01-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2022/3379/3379_2022_4_1505_41177_Judgement_20-Jan-2023.pdf&dno=33792022" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-01-20&dno=33792022&filename=supremecourt/2022/3379/3379_2022_4_1505_41177_Judgement_20-Jan-2023.pdf target="_blank">2023 INSC 66 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>DELHI DEVELOPMENT AUTHORITY</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>BHAGI SINGH</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>NISHIT AGRAWAL</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH, HON'BLE MR. JUSTICE C.T. RAVIKUMAR</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  23</td>
                    <td>Diary Number</td>
                                            <td>3665 / 2021</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-008969-008969 / 2022</td>
                                        <td rowspan="5"><a href="/supremecourt/2021/3665/3665_2021_4_1503_40734_Judgement_05-Jan-2023.pdf" target="_blank"><a href=/supremecourt/2021/3665/3665_2021_4_1503_40734_Judgement_05-Jan-2023.pdf target="_blank">05-01-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2021/3665/3665_2021_4_1503_40734_Judgement_05-Jan-2023.pdf&dno=36652021" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-01-05&dno=36652021&filename=supremecourt/2021/3665/3665_2021_4_1503_40734_Judgement_05-Jan-2023.pdf target="_blank">2023 INSC 14 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>SIDHA NEELKANTH PAPER INDUSTRIES PVT. LTD.</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>PRUDENT ARC LIMITED</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>TUHIN</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH, HON'BLE MR. JUSTICE C.T. RAVIKUMAR</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  24</td>
                    <td>Diary Number</td>
                                            <td>3907 / 2019</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-002030 / 2019</td>
                                        <td rowspan="5"><a href="/supremecourt/2019/3907/3907_2019_1_1501_40710_Judgement_04-Jan-2023.pdf" target="_blank"><a href=/supremecourt/2019/3907/3907_2019_1_1501_40710_Judgement_04-Jan-2023.pdf target="_blank">04-01-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2019/3907/3907_2019_1_1501_40710_Judgement_04-Jan-2023.pdf&dno=39072019" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-01-04&dno=39072019&filename=supremecourt/2019/3907/3907_2019_1_1501_40710_Judgement_04-Jan-2023.pdf target="_blank">2023 INSC 9 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>IFB AGRO INDUSTRIES LIMITED</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>SICGIL INDIA LIMITED</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>E. C. AGRAWALA</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE THE CHIEF JUSTICE, HON'BLE MR. JUSTICE S. ABDUL NAZEER, HON'BLE MR. JUSTICE PAMIDIGHANTAM SRI NARASIMHA</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE THE CHIEF JUSTICE</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  25</td>
                    <td>Diary Number</td>
                                            <td>4395 / 2022</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-004072-004072 / 2022</td>
                                        <td rowspan="5"><a href="/supremecourt/2022/4395/4395_2022_4_1509_41047_Judgement_13-Jan-2023.pdf" target="_blank"><a href=/supremecourt/2022/4395/4395_2022_4_1509_41047_Judgement_13-Jan-2023.pdf target="_blank">13-01-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2022/4395/4395_2022_4_1509_41047_Judgement_13-Jan-2023.pdf&dno=43952022" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-01-13&dno=43952022&filename=supremecourt/2022/4395/4395_2022_4_1509_41047_Judgement_13-Jan-2023.pdf target="_blank">2023 INSC 37 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>C. HARIDASAN</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>ANAPPATH PARAKKATTU VASUDEVAKURUP</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>USHA NANDINI V.</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  26</td>
                    <td>Diary Number</td>
                                            <td>4405 / 2015</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-001811-001812 / 2015</td>
                                        <td rowspan="5"><a href="/supremecourt/2015/4405/4405_2015_4_1501_41935_Judgement_17-Feb-2023.pdf" target="_blank"><a href=/supremecourt/2015/4405/4405_2015_4_1501_41935_Judgement_17-Feb-2023.pdf target="_blank">17-02-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2015/4405/4405_2015_4_1501_41935_Judgement_17-Feb-2023.pdf&dno=44052015" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-02-17&dno=44052015&filename=supremecourt/2015/4405/4405_2015_4_1501_41935_Judgement_17-Feb-2023.pdf target="_blank">2023 INSC 136 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>M/S IL AND FS TAMIL NADU POWER COMPANY LIMITED</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>T. MURUGANANDAM .</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>SENTHIL JAGADEESAN</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH, HON'BLE MR. JUSTICE C.T. RAVIKUMAR</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  27</td>
                    <td>Diary Number</td>
                                            <td>4480 / 2020</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-001669 / 2020</td>
                                        <td rowspan="5"><a href="/supremecourt/2020/4480/4480_2020_4_1501_40713_Judgement_04-Jan-2023.pdf" target="_blank"><a href=/supremecourt/2020/4480/4480_2020_4_1501_40713_Judgement_04-Jan-2023.pdf target="_blank">04-01-2023 <strong>(English)</strong><br><a href=/supremecourt_vernacular/2020/4480/4480_2020_4_1501_40713_Judgement_04-Jan-2023_GUJ.pdf target="_blank">04-01-2023 <strong>(ગુજરાતી)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2020/4480/4480_2020_4_1501_40713_Judgement_04-Jan-2023.pdf&dno=44802020" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-01-04&dno=44802020&filename=supremecourt/2020/4480/4480_2020_4_1501_40713_Judgement_04-Jan-2023.pdf target="_blank">2023 INSC 10 <strong>(English)</strong><br><a href=/pdfdate/index1.php?dt=2023-01-04&dno=44802020&filename=supremecourt_vernacular/2020/4480/4480_2020_4_1501_40713_Judgement_04-Jan-2023_GUJ.pdf target="_blank">2023 INSC 10 <strong>(ગુજરાતી)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>SABARMATI GAS LIMITED</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>SHAH ALLOYS LIMITED</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>SENTHIL JAGADEESAN</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH, HON'BLE MR. JUSTICE C.T. RAVIKUMAR</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE C.T. RAVIKUMAR</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  28</td>
                    <td>Diary Number</td>
                                            <td>4685 / 2021</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-001171-001171 / 2023</td>
                                        <td rowspan="5"><a href="/supremecourt/2021/4685/4685_2021_14_1501_41891_Judgement_15-Feb-2023.pdf" target="_blank"><a href=/supremecourt/2021/4685/4685_2021_14_1501_41891_Judgement_15-Feb-2023.pdf target="_blank">15-02-2023 <strong>(English)</strong><br><a href=/supremecourt_vernacular/2021/4685/4685_2021_14_1501_41891_Judgement_15-Feb-2023_HIN.pdf target="_blank">15-02-2023 <strong>(हिन्दी)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2021/4685/4685_2021_14_1501_41891_Judgement_15-Feb-2023.pdf&dno=46852021" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-02-15&dno=46852021&filename=supremecourt/2021/4685/4685_2021_14_1501_41891_Judgement_15-Feb-2023.pdf target="_blank">2023 INSC 128 <strong>(English)</strong><br><a href=/pdfdate/index1.php?dt=2023-02-15&dno=46852021&filename=supremecourt_vernacular/2021/4685/4685_2021_14_1501_41891_Judgement_15-Feb-2023_HIN.pdf target="_blank">2023 INSC 128 <strong>(हिन्दी)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>PANCHAM LAL PANDEY</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>NEERAJ KUMAR MISHRA</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>PRAVEEN CHATURVEDI</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE V. RAMASUBRAMANIAN, HON'BLE MR. JUSTICE PANKAJ MITHAL</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE V. RAMASUBRAMANIAN</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  29</td>
                    <td>Diary Number</td>
                                            <td>5053 / 2008</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-001890-001891 / 2010</td>
                                        <td rowspan="5"><a href="/supremecourt/2008/5053/5053_2008_3_1501_41786_Judgement_13-Feb-2023.pdf" target="_blank"><a href=/supremecourt/2008/5053/5053_2008_3_1501_41786_Judgement_13-Feb-2023.pdf target="_blank">13-02-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2008/5053/5053_2008_3_1501_41786_Judgement_13-Feb-2023.pdf&dno=50532008" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-02-13&dno=50532008&filename=supremecourt/2008/5053/5053_2008_3_1501_41786_Judgement_13-Feb-2023.pdf target="_blank">2023 INSC 123 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>ASSOCN. OF VASANTH APPTS. OWNERS</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>V. GOPINANTH  AND ORS.</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td>R. NEDUMARAN</td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE K.M. JOSEPH, HON'BLE MRS. JUSTICE B.V. NAGARATHNA</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE K.M. JOSEPH</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  30</td>
                    <td>Diary Number</td>
                                            <td>5112 / 2023</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td> / 0</td>
                                        <td rowspan="5"><a href="/supremecourt/2023/5112/5112_2023_4_301_41777_Judgement_08-Feb-2023.pdf" target="_blank"><a href=/supremecourt/2023/5112/5112_2023_4_301_41777_Judgement_08-Feb-2023.pdf target="_blank">08-02-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2023/5112/5112_2023_4_301_41777_Judgement_08-Feb-2023.pdf&dno=51122023" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-02-08&dno=51122023&filename=supremecourt/2023/5112/5112_2023_4_301_41777_Judgement_08-Feb-2023.pdf target="_blank">2023 INSC 106 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>ASSOCIATION OF OLD SETTLERS OF SIKKIM PRESIDENT SHRI RAM CHANDRA MUNDRA S/O LATE MURLIDHAR MUNDRA</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>UNION OF INDIA  MINISTRY OF FINANCE  SECRETARY GENERAL</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>ANAS TANWIR</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH, HON'BLE MRS. JUSTICE B.V. NAGARATHNA</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  31</td>
                    <td>Diary Number</td>
                                            <td>5241 / 2018</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-000219-000219 / 2023</td>
                                        <td rowspan="5"><a href="/supremecourt/2018/5241/5241_2018_4_1502_41103_Judgement_19-Jan-2023.pdf" target="_blank"><a href=/supremecourt/2018/5241/5241_2018_4_1502_41103_Judgement_19-Jan-2023.pdf target="_blank">19-01-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2018/5241/5241_2018_4_1502_41103_Judgement_19-Jan-2023.pdf&dno=52412018" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-01-19&dno=52412018&filename=supremecourt/2018/5241/5241_2018_4_1502_41103_Judgement_19-Jan-2023.pdf target="_blank">2023 INSC 55 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>UNION OF INDIA</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>CONST. SUNIL KUMAR</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>B. V. BALARAM DAS</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH, HON'BLE MS. JUSTICE HIMA KOHLI</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  32</td>
                    <td>Diary Number</td>
                                            <td>5306 / 2023</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>W.P.(C) No.-000148 / 2023</td>
                                        <td rowspan="5"><a href="/supremecourt/2023/5306/5306_2023_7_1501_41750_Judgement_10-Feb-2023.pdf" target="_blank"><a href=/supremecourt/2023/5306/5306_2023_7_1501_41750_Judgement_10-Feb-2023.pdf target="_blank">10-02-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2023/5306/5306_2023_7_1501_41750_Judgement_10-Feb-2023.pdf&dno=53062023" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-02-10&dno=53062023&filename=supremecourt/2023/5306/5306_2023_7_1501_41750_Judgement_10-Feb-2023.pdf target="_blank">2023 INSC 122 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>ANNA MATHEW</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>SUPREME COURT OF INDIA</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>SANCHITA AIN</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE SANJIV KHANNA, HON'BLE MR. JUSTICE B.R. GAVAI</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE SANJIV KHANNA</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  33</td>
                    <td>Diary Number</td>
                                            <td>5407 / 2019</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-001233-001233 / 2023</td>
                                        <td rowspan="5"><a href="/supremecourt/2019/5407/5407_2019_15_1502_42027_Judgement_20-Feb-2023.pdf" target="_blank"><a href=/supremecourt/2019/5407/5407_2019_15_1502_42027_Judgement_20-Feb-2023.pdf target="_blank">20-02-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2019/5407/5407_2019_15_1502_42027_Judgement_20-Feb-2023.pdf&dno=54072019" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-02-20&dno=54072019&filename=supremecourt/2019/5407/5407_2019_15_1502_42027_Judgement_20-Feb-2023.pdf target="_blank">2023 INSC 142 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>KHORA (DEAD) THROUGH LEGAL HEIRS</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>MOHAR SAI</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>TARUNA SINGH GOHIL</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE V. RAMASUBRAMANIAN, HON'BLE MR. JUSTICE PANKAJ MITHAL</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE V. RAMASUBRAMANIAN</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  34</td>
                    <td>Diary Number</td>
                                            <td>5466 / 2023</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>W.P.(C) No.-000152 / 2023</td>
                                        <td rowspan="5"><a href="/supremecourt/2023/5466/5466_2023_1_40_41933_Judgement_17-Feb-2023.pdf" target="_blank"><a href=/supremecourt/2023/5466/5466_2023_1_40_41933_Judgement_17-Feb-2023.pdf target="_blank">17-02-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2023/5466/5466_2023_1_40_41933_Judgement_17-Feb-2023.pdf&dno=54662023" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-02-17&dno=54662023&filename=supremecourt/2023/5466/5466_2023_1_40_41933_Judgement_17-Feb-2023.pdf target="_blank">2023 INSC 132 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>SHELLY OBEROI</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>OFFICE OF LIEUTENANT GOVERNOR OF DELHI</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>SHADAN FARASAT</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE THE CHIEF JUSTICE, HON'BLE MR. JUSTICE PAMIDIGHANTAM SRI NARASIMHA, HON'BLE MR. JUSTICE J.B. PARDIWALA</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE THE CHIEF JUSTICE</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  35</td>
                    <td>Diary Number</td>
                                            <td>5501 / 2021</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-001355-001356 / 2023</td>
                                        <td rowspan="5"><a href="/supremecourt/2021/5501/5501_2021_7_1501_42020_Judgement_20-Feb-2023.pdf" target="_blank"><a href=/supremecourt/2021/5501/5501_2021_7_1501_42020_Judgement_20-Feb-2023.pdf target="_blank">20-02-2023 <strong>(English)</strong><br><a href=/supremecourt_vernacular/2021/5501/5501_2021_7_1501_42020_Judgement_20-Feb-2023_GUJ.pdf target="_blank">20-02-2023 <strong>(ગુજરાતી)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2021/5501/5501_2021_7_1501_42020_Judgement_20-Feb-2023.pdf&dno=55012021" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-02-20&dno=55012021&filename=supremecourt/2021/5501/5501_2021_7_1501_42020_Judgement_20-Feb-2023.pdf target="_blank">2023 INSC 145 <strong>(English)</strong><br><a href=/pdfdate/index1.php?dt=2023-02-20&dno=55012021&filename=supremecourt_vernacular/2021/5501/5501_2021_7_1501_42020_Judgement_20-Feb-2023_GUJ.pdf target="_blank">2023 INSC 145 <strong>(ગુજરાતી)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>SURESHKUMAR LALITKUMAR PATEL</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>THE STATE OF GUJARAT</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td> PAREKH & CO.</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE SANJIV KHANNA, HON'BLE MR. JUSTICE M.M. SUNDRESH</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE SANJIV KHANNA</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  36</td>
                    <td>Diary Number</td>
                                            <td>5533 / 2022</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-000274-000274 / 2023</td>
                                        <td rowspan="5"><a href="/supremecourt/2022/5533/5533_2022_8_1501_40894_Judgement_10-Jan-2023.pdf" target="_blank"><a href=/supremecourt/2022/5533/5533_2022_8_1501_40894_Judgement_10-Jan-2023.pdf target="_blank">10-01-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2022/5533/5533_2022_8_1501_40894_Judgement_10-Jan-2023.pdf&dno=55332022" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-01-10&dno=55332022&filename=supremecourt/2022/5533/5533_2022_8_1501_40894_Judgement_10-Jan-2023.pdf target="_blank">2023 INSC 22 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>RESIDENTS WELFARE ASSOCIATION</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>THE UNION TERRITORY OF CHANDIGARH</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>ASHOK K. MAHAJAN</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE B.R. GAVAI, HON'BLE MR. JUSTICE M.M. SUNDRESH</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE B.R. GAVAI</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  37</td>
                    <td>Diary Number</td>
                                            <td>5589 / 2022</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-000362-000362 / 2023</td>
                                        <td rowspan="5"><a href="/supremecourt/2022/5589/5589_2022_4_1506_41177_Judgement_20-Jan-2023.pdf" target="_blank"><a href=/supremecourt/2022/5589/5589_2022_4_1506_41177_Judgement_20-Jan-2023.pdf target="_blank">20-01-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2022/5589/5589_2022_4_1506_41177_Judgement_20-Jan-2023.pdf&dno=55892022" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-01-20&dno=55892022&filename=supremecourt/2022/5589/5589_2022_4_1506_41177_Judgement_20-Jan-2023.pdf target="_blank">2023 INSC 67 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>DELHI      DEVELOPMENT AUTHORITY</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>RAMBIR</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>NISHIT AGRAWAL</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH, HON'BLE MR. JUSTICE C.T. RAVIKUMAR</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  38</td>
                    <td>Diary Number</td>
                                            <td>5657 / 2020</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-001276-001277 / 2023</td>
                                        <td rowspan="5"><a href="/supremecourt/2020/5657/5657_2020_4_1501_42249_Judgement_24-Feb-2023.pdf" target="_blank"><a href=/supremecourt/2020/5657/5657_2020_4_1501_42249_Judgement_24-Feb-2023.pdf target="_blank">24-02-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2020/5657/5657_2020_4_1501_42249_Judgement_24-Feb-2023.pdf&dno=56572020" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-02-24&dno=56572020&filename=supremecourt/2020/5657/5657_2020_4_1501_42249_Judgement_24-Feb-2023.pdf target="_blank">2023 INSC 158 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>THE STATE OF HIMACHAL PRADESH</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>CHANDERVIR SINGH NEGI</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>SAMIR ALI KHAN</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH, HON'BLE MR. JUSTICE C.T. RAVIKUMAR</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  39</td>
                    <td>Diary Number</td>
                                            <td>5920 / 2020</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>Crl.A. No.-000549-000549 / 2023</td>
                                        <td rowspan="5"><a href="/supremecourt/2020/5920/5920_2020_9_1501_42078_Judgement_21-Feb-2023.pdf" target="_blank"><a href=/supremecourt/2020/5920/5920_2020_9_1501_42078_Judgement_21-Feb-2023.pdf target="_blank">21-02-2023 <strong>(English)</strong><br><a href=/supremecourt_vernacular/2020/5920/5920_2020_9_1501_42078_Judgement_21-Feb-2023_HIN.pdf target="_blank">21-02-2023 <strong>(हिन्दी)</strong><br><a href=/supremecourt_vernacular/2020/5920/5920_2020_9_1501_42078_Judgement_21-Feb-2023_GUJ.pdf target="_blank">21-02-2023 <strong>(ગુજરાતી)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2020/5920/5920_2020_9_1501_42078_Judgement_21-Feb-2023.pdf&dno=59202020" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-02-21&dno=59202020&filename=supremecourt/2020/5920/5920_2020_9_1501_42078_Judgement_21-Feb-2023.pdf target="_blank">2023 INSC 148 <strong>(English)</strong><br><a href=/pdfdate/index1.php?dt=2023-02-21&dno=59202020&filename=supremecourt_vernacular/2020/5920/5920_2020_9_1501_42078_Judgement_21-Feb-2023_HIN.pdf target="_blank">2023 INSC 148 <strong>(हिन्दी)</strong><br><a href=/pdfdate/index1.php?dt=2023-02-21&dno=59202020&filename=supremecourt_vernacular/2020/5920/5920_2020_9_1501_42078_Judgement_21-Feb-2023_GUJ.pdf target="_blank">2023 INSC 148 <strong>(ગુજરાતી)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>JUHRU</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>KARIM</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>S. K. VERMA</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE SURYA KANT, HON'BLE MR. JUSTICE J.K. MAHESHWARI</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE SURYA KANT</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  40</td>
                    <td>Diary Number</td>
                                            <td>6078 / 2022</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-000363-000363 / 2023</td>
                                        <td rowspan="5"><a href="/supremecourt/2022/6078/6078_2022_4_1507_41177_Judgement_20-Jan-2023.pdf" target="_blank"><a href=/supremecourt/2022/6078/6078_2022_4_1507_41177_Judgement_20-Jan-2023.pdf target="_blank">20-01-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2022/6078/6078_2022_4_1507_41177_Judgement_20-Jan-2023.pdf&dno=60782022" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-01-20&dno=60782022&filename=supremecourt/2022/6078/6078_2022_4_1507_41177_Judgement_20-Jan-2023.pdf target="_blank">2023 INSC 68 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>DELHI DEVELOPMENT AUTHORITY</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>RAJESH DUA</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>MISHRA SAURABH</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH, HON'BLE MR. JUSTICE C.T. RAVIKUMAR</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  41</td>
                    <td>Diary Number</td>
                                            <td>6082 / 2022</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-000364-000364 / 2023</td>
                                        <td rowspan="5"><a href="/supremecourt/2022/6082/6082_2022_4_1508_41177_Judgement_20-Jan-2023.pdf" target="_blank"><a href=/supremecourt/2022/6082/6082_2022_4_1508_41177_Judgement_20-Jan-2023.pdf target="_blank">20-01-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2022/6082/6082_2022_4_1508_41177_Judgement_20-Jan-2023.pdf&dno=60822022" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-01-20&dno=60822022&filename=supremecourt/2022/6082/6082_2022_4_1508_41177_Judgement_20-Jan-2023.pdf target="_blank">2023 INSC 69 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>DELHI DEVELOPMENT AUTHORITY</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>ASHA PRAKASH</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>ASHWANI KUMAR</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH, HON'BLE MR. JUSTICE C.T. RAVIKUMAR</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  42</td>
                    <td>Diary Number</td>
                                            <td>6103 / 2022</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>Crl.A. No.-000634-000634 / 2023</td>
                                        <td rowspan="5"><a href="/supremecourt/2022/6103/6103_2022_12_1501_42413_Judgement_28-Feb-2023.pdf" target="_blank"><a href=/supremecourt/2022/6103/6103_2022_12_1501_42413_Judgement_28-Feb-2023.pdf target="_blank">28-02-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2022/6103/6103_2022_12_1501_42413_Judgement_28-Feb-2023.pdf&dno=61032022" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-02-28&dno=61032022&filename=supremecourt/2022/6103/6103_2022_12_1501_42413_Judgement_28-Feb-2023.pdf target="_blank">2023 INSC 180 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>ROYDEN HAROLD BUTHELLO</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>THE STATE OF CHHATTISGARH</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>JATIN ZAVERI</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE A.S. BOPANNA, HON'BLE MR. JUSTICE AHSANUDDIN AMANULLAH</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE A.S. BOPANNA</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  43</td>
                    <td>Diary Number</td>
                                            <td>6310 / 2023</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>W.P.(C) No.-000190 / 2023</td>
                                        <td rowspan="5"><a href="/supremecourt/2023/6310/6310_2023_3_23_42310_Judgement_27-Feb-2023.pdf" target="_blank"><a href=/supremecourt/2023/6310/6310_2023_3_23_42310_Judgement_27-Feb-2023.pdf target="_blank">27-02-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2023/6310/6310_2023_3_23_42310_Judgement_27-Feb-2023.pdf&dno=63102023" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-02-27&dno=63102023&filename=supremecourt/2023/6310/6310_2023_3_23_42310_Judgement_27-Feb-2023.pdf target="_blank">2023 INSC 174 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>ASHWINI KUMAR UPADHYAY</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>UNION OF INDIA</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>ASHWANI KUMAR DUBEY</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE K.M. JOSEPH, HON'BLE MRS. JUSTICE B.V. NAGARATHNA</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE K.M. JOSEPH</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  44</td>
                    <td>Diary Number</td>
                                            <td>6826 / 2014</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>Crl.A. No.-000609-000609 / 2015</td>
                                        <td rowspan="5"><a href="/supremecourt/2014/6826/6826_2014_8_1501_42388_Judgement_28-Feb-2023.pdf" target="_blank"><a href=/supremecourt/2014/6826/6826_2014_8_1501_42388_Judgement_28-Feb-2023.pdf target="_blank">28-02-2023 <strong>(English)</strong><br><a href=/supremecourt_vernacular/2014/6826/6826_2014_8_1501_42388_Judgement_28-Feb-2023_BEN.pdf target="_blank">28-02-2023 <strong>(বাংলা)</strong><br><a href=/supremecourt_vernacular/2014/6826/6826_2014_8_1501_42388_Judgement_28-Feb-2023_GUJ.pdf target="_blank">28-02-2023 <strong>(ગુજરાતી)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2014/6826/6826_2014_8_1501_42388_Judgement_28-Feb-2023.pdf&dno=68262014" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-02-28&dno=68262014&filename=supremecourt/2014/6826/6826_2014_8_1501_42388_Judgement_28-Feb-2023.pdf target="_blank">2023 INSC 175 <strong>(English)</strong><br><a href=/pdfdate/index1.php?dt=2023-02-28&dno=68262014&filename=supremecourt_vernacular/2014/6826/6826_2014_8_1501_42388_Judgement_28-Feb-2023_BEN.pdf target="_blank">2023 INSC 175 <strong>(বাংলা)</strong><br><a href=/pdfdate/index1.php?dt=2023-02-28&dno=68262014&filename=supremecourt_vernacular/2014/6826/6826_2014_8_1501_42388_Judgement_28-Feb-2023_GUJ.pdf target="_blank">2023 INSC 175 <strong>(ગુજરાતી)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>INDRAJIT DAS</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>THE STATE OF TRIPURA</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>MADHUMITA BHATTACHARJEE</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE B.R. GAVAI, HON'BLE MR. JUSTICE VIKRAM NATH, HON'BLE MR. JUSTICE SANJAY KAROL</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE VIKRAM NATH</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  45</td>
                    <td>Diary Number</td>
                                            <td>6958 / 2018</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-000733-000733 / 2023</td>
                                        <td rowspan="5"><a href="/supremecourt/2018/6958/6958_2018_4_1501_41722_Judgement_09-Feb-2023.pdf" target="_blank"><a href=/supremecourt/2018/6958/6958_2018_4_1501_41722_Judgement_09-Feb-2023.pdf target="_blank">09-02-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2018/6958/6958_2018_4_1501_41722_Judgement_09-Feb-2023.pdf&dno=69582018" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-02-09&dno=69582018&filename=supremecourt/2018/6958/6958_2018_4_1501_41722_Judgement_09-Feb-2023.pdf target="_blank">2023 INSC 107 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>NORTH DELHI MUNICIPAL CORPORATION THROUGH ITS COMMISSIONER</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>RAM CHNADER SINGH</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>PRAVEEN SWARUP</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH, HON'BLE MR. JUSTICE C.T. RAVIKUMAR, HON'BLE MR. JUSTICE SANJAY KAROL</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  46</td>
                    <td>Diary Number</td>
                                            <td>7125 / 2022</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-000365-000365 / 2023</td>
                                        <td rowspan="5"><a href="/supremecourt/2022/7125/7125_2022_4_1509_41177_Judgement_20-Jan-2023.pdf" target="_blank"><a href=/supremecourt/2022/7125/7125_2022_4_1509_41177_Judgement_20-Jan-2023.pdf target="_blank">20-01-2023 <strong>(English)</strong><br><a href=/supremecourt_vernacular/2022/7125/7125_2022_4_1509_41177_Judgement_20-Jan-2023_HIN.pdf target="_blank">20-01-2023 <strong>(हिन्दी)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2022/7125/7125_2022_4_1509_41177_Judgement_20-Jan-2023.pdf&dno=71252022" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-01-20&dno=71252022&filename=supremecourt/2022/7125/7125_2022_4_1509_41177_Judgement_20-Jan-2023.pdf target="_blank">2023 INSC 70 <strong>(English)</strong><br><a href=/pdfdate/index1.php?dt=2023-01-20&dno=71252022&filename=supremecourt_vernacular/2022/7125/7125_2022_4_1509_41177_Judgement_20-Jan-2023_HIN.pdf target="_blank">2023 INSC 70 <strong>(हिन्दी)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>DELHI DEVELOPMENT AUTHORITY</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>SHYAMO</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>BINU TAMTA</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH, HON'BLE MR. JUSTICE C.T. RAVIKUMAR</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  47</td>
                    <td>Diary Number</td>
                                            <td>7194 / 2022</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>Crl.A. No.-000586-000586 / 2023</td>
                                        <td rowspan="5"><a href="/supremecourt/2022/7194/7194_2022_4_1504_42249_Judgement_24-Feb-2023.pdf" target="_blank"><a href=/supremecourt/2022/7194/7194_2022_4_1504_42249_Judgement_24-Feb-2023.pdf target="_blank">24-02-2023 <strong>(English)</strong><br><a href=/supremecourt_vernacular/2022/7194/7194_2022_4_1504_42249_Judgement_24-Feb-2023_HIN.pdf target="_blank">24-02-2023 <strong>(हिन्दी)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2022/7194/7194_2022_4_1504_42249_Judgement_24-Feb-2023.pdf&dno=71942022" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-02-24&dno=71942022&filename=supremecourt/2022/7194/7194_2022_4_1504_42249_Judgement_24-Feb-2023.pdf target="_blank">2023 INSC 160 <strong>(English)</strong><br><a href=/pdfdate/index1.php?dt=2023-02-24&dno=71942022&filename=supremecourt_vernacular/2022/7194/7194_2022_4_1504_42249_Judgement_24-Feb-2023_HIN.pdf target="_blank">2023 INSC 160 <strong>(हिन्दी)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>THE STATE OF MADHYA PRADESH</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>JAD BAI,</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>PASHUPATHI NATH RAZDAN</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH, HON'BLE MR. JUSTICE C.T. RAVIKUMAR</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  48</td>
                    <td>Diary Number</td>
                                            <td>7205 / 2022</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-001301-001301 / 2023</td>
                                        <td rowspan="5"><a href="/supremecourt/2022/7205/7205_2022_4_1505_42249_Judgement_24-Feb-2023.pdf" target="_blank"><a href=/supremecourt/2022/7205/7205_2022_4_1505_42249_Judgement_24-Feb-2023.pdf target="_blank">24-02-2023 <strong>(English)</strong><br><a href=/supremecourt_vernacular/2022/7205/7205_2022_4_1505_42249_Judgement_24-Feb-2023_HIN.pdf target="_blank">24-02-2023 <strong>(हिन्दी)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2022/7205/7205_2022_4_1505_42249_Judgement_24-Feb-2023.pdf&dno=72052022" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-02-24&dno=72052022&filename=supremecourt/2022/7205/7205_2022_4_1505_42249_Judgement_24-Feb-2023.pdf target="_blank">2023 INSC 165 <strong>(English)</strong><br><a href=/pdfdate/index1.php?dt=2023-02-24&dno=72052022&filename=supremecourt_vernacular/2022/7205/7205_2022_4_1505_42249_Judgement_24-Feb-2023_HIN.pdf target="_blank">2023 INSC 165 <strong>(हिन्दी)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>DELHI DEVELOPMENT AUTHORITY</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>RAJENDER SINGH</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>MANIKA TRIPATHY</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH, HON'BLE MR. JUSTICE C.T. RAVIKUMAR</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  49</td>
                    <td>Diary Number</td>
                                            <td>7441 / 2022</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-008962-008963 / 2022</td>
                                        <td rowspan="5"><a href="/supremecourt/2022/7441/7441_2022_4_1506_40734_Judgement_05-Jan-2023.pdf" target="_blank"><a href=/supremecourt/2022/7441/7441_2022_4_1506_40734_Judgement_05-Jan-2023.pdf target="_blank">05-01-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2022/7441/7441_2022_4_1506_40734_Judgement_05-Jan-2023.pdf&dno=74412022" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-01-05&dno=74412022&filename=supremecourt/2022/7441/7441_2022_4_1506_40734_Judgement_05-Jan-2023.pdf target="_blank">2023 INSC 19 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>BASAVARAJ</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>PADMAVATHI</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>NISHANTH PATIL</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH, HON'BLE MR. JUSTICE C.T. RAVIKUMAR</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  50</td>
                    <td>Diary Number</td>
                                            <td>8031 / 2019</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-000342-000342 / 2023</td>
                                        <td rowspan="5"><a href="/supremecourt/2019/8031/8031_2019_4_1501_41177_Judgement_20-Jan-2023.pdf" target="_blank"><a href=/supremecourt/2019/8031/8031_2019_4_1501_41177_Judgement_20-Jan-2023.pdf target="_blank">20-01-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2019/8031/8031_2019_4_1501_41177_Judgement_20-Jan-2023.pdf&dno=80312019" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-01-20&dno=80312019&filename=supremecourt/2019/8031/8031_2019_4_1501_41177_Judgement_20-Jan-2023.pdf target="_blank">2023 INSC 62 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>DELHI DEVELOPMENT AUTHORITY VICE CHAIRMAN</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>SHAKUNTLA DEVI</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>ASHWANI KUMAR</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH, HON'BLE MR. JUSTICE C.T. RAVIKUMAR</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  51</td>
                    <td>Diary Number</td>
                                            <td>8339 / 2020</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-000523-000523 / 2023</td>
                                        <td rowspan="5"><a href="/supremecourt/2020/8339/8339_2020_8_1501_41274_Judgement_25-Jan-2023.pdf" target="_blank"><a href=/supremecourt/2020/8339/8339_2020_8_1501_41274_Judgement_25-Jan-2023.pdf target="_blank">25-01-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2020/8339/8339_2020_8_1501_41274_Judgement_25-Jan-2023.pdf&dno=83392020" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-01-25&dno=83392020&filename=supremecourt/2020/8339/8339_2020_8_1501_41274_Judgement_25-Jan-2023.pdf target="_blank">2023 INSC 84 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>DEVELOPER GROUP INDIA PVT. LTD.</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>SURINDER SINGH MARWAH</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE B.R. GAVAI, HON'BLE MR. JUSTICE VIKRAM NATH</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE B.R. GAVAI</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  52</td>
                    <td>Diary Number</td>
                                            <td>8544 / 2023</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>W.P.(C) No.-000302 / 2023</td>
                                        <td rowspan="5"><a href="/supremecourt/2023/8544/8544_2023_1_301_42566_Judgement_28-Feb-2023.pdf" target="_blank"><a href=/supremecourt/2023/8544/8544_2023_1_301_42566_Judgement_28-Feb-2023.pdf target="_blank">28-02-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2023/8544/8544_2023_1_301_42566_Judgement_28-Feb-2023.pdf&dno=85442023" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-02-28&dno=85442023&filename=supremecourt/2023/8544/8544_2023_1_301_42566_Judgement_28-Feb-2023.pdf target="_blank">2023 INSC 181 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>THE STATE OF PUNJAB</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>PRINCIPAL SECRETARY TO THE GOVERNOR OF PUNJAB</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>SHADAN FARASAT</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE THE CHIEF JUSTICE, HON'BLE MR. JUSTICE PAMIDIGHANTAM SRI NARASIMHA</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE THE CHIEF JUSTICE</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  53</td>
                    <td>Diary Number</td>
                                            <td>8571 / 2022</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-000966-000966 / 2023</td>
                                        <td rowspan="5"><a href="/supremecourt/2022/8571/8571_2022_1_32_41733_Judgement_10-Feb-2023.pdf" target="_blank"><a href=/supremecourt/2022/8571/8571_2022_1_32_41733_Judgement_10-Feb-2023.pdf target="_blank">10-02-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2022/8571/8571_2022_1_32_41733_Judgement_10-Feb-2023.pdf&dno=85712022" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-02-10&dno=85712022&filename=supremecourt/2022/8571/8571_2022_1_32_41733_Judgement_10-Feb-2023.pdf target="_blank">2023 INSC 117 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>NATIONAL MEDICAL COMMISSION</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>ANNASAHEB CHUDAMAN PATIL MEMORIAL MEDICAL COLLEGE</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>GAURAV SHARMA</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE THE CHIEF JUSTICE, HON'BLE MR. JUSTICE PAMIDIGHANTAM SRI NARASIMHA, HON'BLE MR. JUSTICE J.B. PARDIWALA</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE THE CHIEF JUSTICE</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  54</td>
                    <td>Diary Number</td>
                                            <td>9025 / 2021</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-001278-001278 / 2023</td>
                                        <td rowspan="5"><a href="/supremecourt/2021/9025/9025_2021_4_1512_42249_Judgement_24-Feb-2023.pdf" target="_blank"><a href=/supremecourt/2021/9025/9025_2021_4_1512_42249_Judgement_24-Feb-2023.pdf target="_blank">24-02-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2021/9025/9025_2021_4_1512_42249_Judgement_24-Feb-2023.pdf&dno=90252021" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-02-24&dno=90252021&filename=supremecourt/2021/9025/9025_2021_4_1512_42249_Judgement_24-Feb-2023.pdf target="_blank">2023 INSC 159 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>THE STATE OF HIMACHAL PRADESH</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>RAJIV</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>SAMIR ALI KHAN</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td>RADHIKA GAUTAM</td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH, HON'BLE MR. JUSTICE C.T. RAVIKUMAR</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  55</td>
                    <td>Diary Number</td>
                                            <td>9266 / 2013</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-003893-003893 / 2013</td>
                                        <td rowspan="5"><a href="/supremecourt/2013/9266/9266_2013_5_1501_41655_Judgement_09-Feb-2023.pdf" target="_blank"><a href=/supremecourt/2013/9266/9266_2013_5_1501_41655_Judgement_09-Feb-2023.pdf target="_blank">09-02-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2013/9266/9266_2013_5_1501_41655_Judgement_09-Feb-2023.pdf&dno=92662013" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-02-09&dno=92662013&filename=supremecourt/2013/9266/9266_2013_5_1501_41655_Judgement_09-Feb-2023.pdf target="_blank">2023 INSC 112 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>KARNAVATI VENNERS PVT. LTD.</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>NEW INDIA ASSURANCE CO. LTD. .</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>SHUBHANGI TULI</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE AJAY RASTOGI, HON'BLE MS. JUSTICE BELA M. TRIVEDI</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE AJAY RASTOGI</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  56</td>
                    <td>Diary Number</td>
                                            <td>9598 / 2022</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>W.P.(C) No.-000237 / 2022</td>
                                        <td rowspan="5"><a href="/supremecourt/2022/9598/9598_2022_16_1501_41932_Judgement_13-Feb-2023.pdf" target="_blank"><a href=/supremecourt/2022/9598/9598_2022_16_1501_41932_Judgement_13-Feb-2023.pdf target="_blank">13-02-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2022/9598/9598_2022_16_1501_41932_Judgement_13-Feb-2023.pdf&dno=95982022" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-02-13&dno=95982022&filename=supremecourt/2022/9598/9598_2022_16_1501_41932_Judgement_13-Feb-2023.pdf target="_blank">2023 INSC 124 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>HAJI ABDUL GANI KHAN</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>UNION OF INDIA</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>SRIRAM P.</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE ABHAY S. OKA, HON'BLE MR. JUSTICE RAJESH BINDAL</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE ABHAY S. OKA</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  57</td>
                    <td>Diary Number</td>
                                            <td>9638 / 2021</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-000739-000739 / 2023</td>
                                        <td rowspan="5"><a href="/supremecourt/2021/9638/9638_2021_4_1503_41722_Judgement_09-Feb-2023.pdf" target="_blank"><a href=/supremecourt/2021/9638/9638_2021_4_1503_41722_Judgement_09-Feb-2023.pdf target="_blank">09-02-2023 <strong>(English)</strong><br><a href=/supremecourt_vernacular/2021/9638/9638_2021_4_1503_41722_Judgement_09-Feb-2023_HIN.pdf target="_blank">09-02-2023 <strong>(हिन्दी)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2021/9638/9638_2021_4_1503_41722_Judgement_09-Feb-2023.pdf&dno=96382021" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-02-09&dno=96382021&filename=supremecourt/2021/9638/9638_2021_4_1503_41722_Judgement_09-Feb-2023.pdf target="_blank">2023 INSC 108 <strong>(English)</strong><br><a href=/pdfdate/index1.php?dt=2023-02-09&dno=96382021&filename=supremecourt_vernacular/2021/9638/9638_2021_4_1503_41722_Judgement_09-Feb-2023_HIN.pdf target="_blank">2023 INSC 108 <strong>(हिन्दी)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>GOVERNMENT OF NCT OF DELHI LAND AND BUILDING DEPARTMENT</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>SHAKEEL AHMED</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>SUJEETA SRIVASTAVA</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH, HON'BLE MR. JUSTICE C.T. RAVIKUMAR, HON'BLE MR. JUSTICE SANJAY KAROL</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  58</td>
                    <td>Diary Number</td>
                                            <td>9691 / 2022</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-001308-001308 / 2023</td>
                                        <td rowspan="5"><a href="/supremecourt/2022/9691/9691_2022_15_1501_42221_Judgement_20-Feb-2023.pdf" target="_blank"><a href=/supremecourt/2022/9691/9691_2022_15_1501_42221_Judgement_20-Feb-2023.pdf target="_blank">20-02-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2022/9691/9691_2022_15_1501_42221_Judgement_20-Feb-2023.pdf&dno=96912022" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-02-20&dno=96912022&filename=supremecourt/2022/9691/9691_2022_15_1501_42221_Judgement_20-Feb-2023.pdf target="_blank">2023 INSC 146 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>APARNA AJINKYA FIRODIA</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>AJINKYA ARUN FIRODIA</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>SANYAT LODHA</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE V. RAMASUBRAMANIAN, HON'BLE MRS. JUSTICE B.V. NAGARATHNA</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE V. RAMASUBRAMANIAN</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  59</td>
                    <td>Diary Number</td>
                                            <td>9702 / 2022</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-000172-000172 / 2023</td>
                                        <td rowspan="5"><a href="/supremecourt/2022/9702/9702_2022_4_1502_40999_Judgement_16-Jan-2023.pdf" target="_blank"><a href=/supremecourt/2022/9702/9702_2022_4_1502_40999_Judgement_16-Jan-2023.pdf target="_blank">16-01-2023 <strong>(English)</strong><br><a href=/supremecourt_vernacular/2022/9702/9702_2022_4_1502_40999_Judgement_16-Jan-2023_GUJ.pdf target="_blank">16-01-2023 <strong>(ગુજરાતી)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2022/9702/9702_2022_4_1502_40999_Judgement_16-Jan-2023.pdf&dno=97022022" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-01-16&dno=97022022&filename=supremecourt/2022/9702/9702_2022_4_1502_40999_Judgement_16-Jan-2023.pdf target="_blank">2023 INSC 41 <strong>(English)</strong><br><a href=/pdfdate/index1.php?dt=2023-01-16&dno=97022022&filename=supremecourt_vernacular/2022/9702/9702_2022_4_1502_40999_Judgement_16-Jan-2023_GUJ.pdf target="_blank">2023 INSC 41 <strong>(ગુજરાતી)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>THE UNION OF INDIA</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>RAJIB KHAN</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>ARVIND KUMAR SHARMA</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH, HON'BLE MR. JUSTICE C.T. RAVIKUMAR</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  60</td>
                    <td>Diary Number</td>
                                            <td>9801 / 2022</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-001300-001300 / 2023</td>
                                        <td rowspan="5"><a href="/supremecourt/2022/9801/9801_2022_4_1506_42249_Judgement_24-Feb-2023.pdf" target="_blank"><a href=/supremecourt/2022/9801/9801_2022_4_1506_42249_Judgement_24-Feb-2023.pdf target="_blank">24-02-2023 <strong>(English)</strong><br><a href=/supremecourt_vernacular/2022/9801/9801_2022_4_1506_42249_Judgement_24-Feb-2023_HIN.pdf target="_blank">24-02-2023 <strong>(हिन्दी)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2022/9801/9801_2022_4_1506_42249_Judgement_24-Feb-2023.pdf&dno=98012022" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-02-24&dno=98012022&filename=supremecourt/2022/9801/9801_2022_4_1506_42249_Judgement_24-Feb-2023.pdf target="_blank">2023 INSC 166 <strong>(English)</strong><br><a href=/pdfdate/index1.php?dt=2023-02-24&dno=98012022&filename=supremecourt_vernacular/2022/9801/9801_2022_4_1506_42249_Judgement_24-Feb-2023_HIN.pdf target="_blank">2023 INSC 166 <strong>(हिन्दी)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>LAND ACQUISITION COLLECTOR</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>JAI PRAKASH TYAGI</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>ASTHA TYAGI</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH, HON'BLE MR. JUSTICE C.T. RAVIKUMAR</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  61</td>
                    <td>Diary Number</td>
                                            <td>9905 / 2022</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-001241-001242 / 2023</td>
                                        <td rowspan="5"><a href="/supremecourt/2022/9905/9905_2022_8_1501_41864_Judgement_16-Feb-2023.pdf" target="_blank"><a href=/supremecourt/2022/9905/9905_2022_8_1501_41864_Judgement_16-Feb-2023.pdf target="_blank">16-02-2023 <strong>(English)</strong><br><a href=/supremecourt_vernacular/2022/9905/9905_2022_8_1501_41864_Judgement_16-Feb-2023_GUJ.pdf target="_blank">16-02-2023 <strong>(ગુજરાતી)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2022/9905/9905_2022_8_1501_41864_Judgement_16-Feb-2023.pdf&dno=99052022" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-02-16&dno=99052022&filename=supremecourt/2022/9905/9905_2022_8_1501_41864_Judgement_16-Feb-2023.pdf target="_blank">2023 INSC 130 <strong>(English)</strong><br><a href=/pdfdate/index1.php?dt=2023-02-16&dno=99052022&filename=supremecourt_vernacular/2022/9905/9905_2022_8_1501_41864_Judgement_16-Feb-2023_GUJ.pdf target="_blank">2023 INSC 130 <strong>(ગુજરાતી)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>CHAUS TAUSHIF ALIMIYA</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>MEMON MAHMMAD UMAR ANWARBHAI</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>VIKALP MUDGAL</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE B.R. GAVAI, HON'BLE MR. JUSTICE VIKRAM NATH, HON'BLE MR. JUSTICE SANJAY KAROL</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE VIKRAM NATH</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  62</td>
                    <td>Diary Number</td>
                                            <td>9921 / 2022</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-001347-001349 / 2023</td>
                                        <td rowspan="5"><a href="/supremecourt/2022/9921/9921_2022_4_1507_42249_Judgement_24-Feb-2023.pdf" target="_blank"><a href=/supremecourt/2022/9921/9921_2022_4_1507_42249_Judgement_24-Feb-2023.pdf target="_blank">24-02-2023 <strong>(English)</strong><br><a href=/supremecourt_vernacular/2022/9921/9921_2022_4_1507_42249_Judgement_24-Feb-2023_HIN.pdf target="_blank">24-02-2023 <strong>(हिन्दी)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2022/9921/9921_2022_4_1507_42249_Judgement_24-Feb-2023.pdf&dno=99212022" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-02-24&dno=99212022&filename=supremecourt/2022/9921/9921_2022_4_1507_42249_Judgement_24-Feb-2023.pdf target="_blank">2023 INSC 167 <strong>(English)</strong><br><a href=/pdfdate/index1.php?dt=2023-02-24&dno=99212022&filename=supremecourt_vernacular/2022/9921/9921_2022_4_1507_42249_Judgement_24-Feb-2023_HIN.pdf target="_blank">2023 INSC 167 <strong>(हिन्दी)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>STATE OF HARYANA</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>NIRANJAN SINGH</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>MONIKA GUSAIN</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH, HON'BLE MR. JUSTICE C.T. RAVIKUMAR</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  63</td>
                    <td>Diary Number</td>
                                            <td>10151 / 2021</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-001384-001385 / 2023</td>
                                        <td rowspan="5"><a href="/supremecourt/2021/10151/10151_2021_5_1502_42140_Judgement_23-Feb-2023.pdf" target="_blank"><a href=/supremecourt/2021/10151/10151_2021_5_1502_42140_Judgement_23-Feb-2023.pdf target="_blank">23-02-2023 <strong>(English)</strong><br><a href=/supremecourt_vernacular/2021/10151/10151_2021_5_1502_42140_Judgement_23-Feb-2023_ORI.pdf target="_blank">23-02-2023 <strong>(ଓଡ଼ିଆ)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2021/10151/10151_2021_5_1502_42140_Judgement_23-Feb-2023.pdf&dno=101512021" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-02-23&dno=101512021&filename=supremecourt/2021/10151/10151_2021_5_1502_42140_Judgement_23-Feb-2023.pdf target="_blank">2023 INSC 154 <strong>(English)</strong><br><a href=/pdfdate/index1.php?dt=2023-02-23&dno=101512021&filename=supremecourt_vernacular/2021/10151/10151_2021_5_1502_42140_Judgement_23-Feb-2023_ORI.pdf target="_blank">2023 INSC 154 <strong>(ଓଡ଼ିଆ)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>OFFICE OF THE ODISHA LOKAYUKTA</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>PRADEEP KUMAR PANIGRAHI</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>ARJUN GARG</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE AJAY RASTOGI, HON'BLE MS. JUSTICE BELA M. TRIVEDI</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE AJAY RASTOGI</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  64</td>
                    <td>Diary Number</td>
                                            <td>10252 / 2017</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-000521-000522 / 2023</td>
                                        <td rowspan="5"><a href="/supremecourt/2017/10252/10252_2017_3_1501_41294_Judgement_25-Jan-2023.pdf" target="_blank"><a href=/supremecourt/2017/10252/10252_2017_3_1501_41294_Judgement_25-Jan-2023.pdf target="_blank">25-01-2023 <strong>(English)</strong><br><a href=/supremecourt_vernacular/2017/10252/10252_2017_3_1501_41294_Judgement_25-Jan-2023_TAM.pdf target="_blank">25-01-2023 <strong>(தமிழ்)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2017/10252/10252_2017_3_1501_41294_Judgement_25-Jan-2023.pdf&dno=102522017" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-01-25&dno=102522017&filename=supremecourt/2017/10252/10252_2017_3_1501_41294_Judgement_25-Jan-2023.pdf target="_blank">2023 INSC 83 <strong>(English)</strong><br><a href=/pdfdate/index1.php?dt=2023-01-25&dno=102522017&filename=supremecourt_vernacular/2017/10252/10252_2017_3_1501_41294_Judgement_25-Jan-2023_TAM.pdf target="_blank">2023 INSC 83 <strong>(தமிழ்)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>ELUMALAI @ VENKATESAN  AND ANR.</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>M KAMALA AND ORS ETC.</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>P. V. YOGESWARAN</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE K.M. JOSEPH, HON'BLE MR. JUSTICE AJAY RASTOGI, HON'BLE MR. JUSTICE ANIRUDDHA BOSE, HON'BLE MR. JUSTICE HRISHIKESH ROY, HON'BLE MR. JUSTICE C.T. RAVIKUMAR</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE K.M. JOSEPH</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  65</td>
                    <td>Diary Number</td>
                                            <td>10389 / 2021</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>Crl.A. No.-001555-001555 / 2022</td>
                                        <td rowspan="5"><a href="/supremecourt/2021/10389/10389_2021_4_1504_40734_Judgement_05-Jan-2023.pdf" target="_blank"><a href=/supremecourt/2021/10389/10389_2021_4_1504_40734_Judgement_05-Jan-2023.pdf target="_blank">05-01-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2021/10389/10389_2021_4_1504_40734_Judgement_05-Jan-2023.pdf&dno=103892021" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-01-05&dno=103892021&filename=supremecourt/2021/10389/10389_2021_4_1504_40734_Judgement_05-Jan-2023.pdf target="_blank">2023 INSC 18 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>B. VENKATESWARAN</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>P. BAKTHAVATCHALAM</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>PRANAB PRAKASH</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH, HON'BLE MR. JUSTICE C.T. RAVIKUMAR</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  66</td>
                    <td>Diary Number</td>
                                            <td>10415 / 2022</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-000350-000350 / 2023</td>
                                        <td rowspan="5"><a href="/supremecourt/2022/10415/10415_2022_4_1510_41177_Judgement_20-Jan-2023.pdf" target="_blank"><a href=/supremecourt/2022/10415/10415_2022_4_1510_41177_Judgement_20-Jan-2023.pdf target="_blank">20-01-2023 <strong>(English)</strong><br><a href=/supremecourt_vernacular/2022/10415/10415_2022_4_1510_41177_Judgement_20-Jan-2023_ASM.pdf target="_blank">20-01-2023 <strong>(অসমীয়া)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2022/10415/10415_2022_4_1510_41177_Judgement_20-Jan-2023.pdf&dno=104152022" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-01-20&dno=104152022&filename=supremecourt/2022/10415/10415_2022_4_1510_41177_Judgement_20-Jan-2023.pdf target="_blank">2023 INSC 59 <strong>(English)</strong><br><a href=/pdfdate/index1.php?dt=2023-01-20&dno=104152022&filename=supremecourt_vernacular/2022/10415/10415_2022_4_1510_41177_Judgement_20-Jan-2023_ASM.pdf target="_blank">2023 INSC 59 <strong>(অসমীয়া)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>THE ARUNACHAL PRADESH PUBLIC SERVICE COMMISSION (APPSC)</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>MISS HAGE MAMUNG</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>ANIL SHRIVASTAV</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH, HON'BLE MR. JUSTICE C.T. RAVIKUMAR</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  67</td>
                    <td>Diary Number</td>
                                            <td>10895 / 2009</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>Crl.A. No.-001439-001439 / 2009</td>
                                        <td rowspan="5"><a href="/supremecourt/2009/10895/10895_2009_8_102_40920_Judgement_12-Jan-2023.pdf" target="_blank"><a href=/supremecourt/2009/10895/10895_2009_8_102_40920_Judgement_12-Jan-2023.pdf target="_blank">12-01-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2009/10895/10895_2009_8_102_40920_Judgement_12-Jan-2023.pdf&dno=108952009" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-01-12&dno=108952009&filename=supremecourt/2009/10895/10895_2009_8_102_40920_Judgement_12-Jan-2023.pdf target="_blank">2023 INSC 23 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>BOBY</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>STATE OF KERALA</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>P. S. SUDHEER</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td>G. PRAKASH</td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE B.R. GAVAI, HON'BLE MR. JUSTICE M.M. SUNDRESH</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE B.R. GAVAI</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  68</td>
                    <td>Diary Number</td>
                                            <td>11669 / 2021</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>SLP(C) No.-008442 / 2021</td>
                                        <td rowspan="5"><a href="/supremecourt/2021/11669/11669_2021_12_1501_41263_Judgement_24-Jan-2023.pdf" target="_blank"><a href=/supremecourt/2021/11669/11669_2021_12_1501_41263_Judgement_24-Jan-2023.pdf target="_blank">24-01-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2021/11669/11669_2021_12_1501_41263_Judgement_24-Jan-2023.pdf&dno=116692021" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-01-24&dno=116692021&filename=supremecourt/2021/11669/11669_2021_12_1501_41263_Judgement_24-Jan-2023.pdf target="_blank">2023 INSC 82 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>FISHERMAN CARE</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>THE GOVERNMENT OF INDIA DEPARTMENT OF ANIMAL HUSBANDRY, DAIRYING AND FISHERIES  REP. BY ITS SECRETARY</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>M.P. PARTHIBAN</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE A.S. BOPANNA</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  69</td>
                    <td>Diary Number</td>
                                            <td>12419 / 2019</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-000716-000716 / 2023</td>
                                        <td rowspan="5"><a href="/supremecourt/2019/12419/12419_2019_13_1501_41405_Judgement_31-Jan-2023.pdf" target="_blank"><a href=/supremecourt/2019/12419/12419_2019_13_1501_41405_Judgement_31-Jan-2023.pdf target="_blank">31-01-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2019/12419/12419_2019_13_1501_41405_Judgement_31-Jan-2023.pdf&dno=124192019" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-01-31&dno=124192019&filename=supremecourt/2019/12419/12419_2019_13_1501_41405_Judgement_31-Jan-2023.pdf target="_blank">2023 INSC 90 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>AJAY DABRA</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>PYARE RAM</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>BHAGABATI PRASAD PADHY</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE KRISHNA MURARI, HON'BLE MR. JUSTICE SUDHANSHU DHULIA</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE KRISHNA MURARI</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  70</td>
                    <td>Diary Number</td>
                                            <td>12564 / 2009</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>Crl.A. No.-002010-002010 / 2010</td>
                                        <td rowspan="5"><a href="/supremecourt/2009/12564/12564_2009_8_104_40920_Judgement_12-Jan-2023.pdf" target="_blank"><a href=/supremecourt/2009/12564/12564_2009_8_104_40920_Judgement_12-Jan-2023.pdf target="_blank">12-01-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2009/12564/12564_2009_8_104_40920_Judgement_12-Jan-2023.pdf&dno=125642009" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-01-12&dno=125642009&filename=supremecourt/2009/12564/12564_2009_8_104_40920_Judgement_12-Jan-2023.pdf target="_blank">2023 INSC 24 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>PRAKASH NAYI @ SEN</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>THE STATE OF GOA</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>AFTAB ALI KHAN</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE B.R. GAVAI, HON'BLE MR. JUSTICE M.M. SUNDRESH</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE M.M. SUNDRESH</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  71</td>
                    <td>Diary Number</td>
                                            <td>12570 / 2009</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>Crl.A. No.-000636-000636 / 2010</td>
                                        <td rowspan="5"><a href="/supremecourt/2009/12570/12570_2009_8_110_41086_Judgement_18-Jan-2023.pdf" target="_blank"><a href=/supremecourt/2009/12570/12570_2009_8_110_41086_Judgement_18-Jan-2023.pdf target="_blank">18-01-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2009/12570/12570_2009_8_110_41086_Judgement_18-Jan-2023.pdf&dno=125702009" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-01-18&dno=125702009&filename=supremecourt/2009/12570/12570_2009_8_110_41086_Judgement_18-Jan-2023.pdf target="_blank">2023 INSC 52 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>STALIN @ SATALIN SAMUVEL</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>STATE REP. BY THE INSPECTOR OF POLICE</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>K. PAARI VENDHAN</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td>M. YOGESH KANNA</td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE B.R. GAVAI, HON'BLE MR. JUSTICE VIKRAM NATH</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE B.R. GAVAI</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  72</td>
                    <td>Diary Number</td>
                                            <td>12892 / 2022</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>Crl.A. No.-002328-002328 / 2022</td>
                                        <td rowspan="5"><a href="/supremecourt/2022/12892/12892_2022_8_1501_40677_Judgement_02-Jan-2023.pdf" target="_blank"><a href=/supremecourt/2022/12892/12892_2022_8_1501_40677_Judgement_02-Jan-2023.pdf target="_blank">02-01-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2022/12892/12892_2022_8_1501_40677_Judgement_02-Jan-2023.pdf&dno=128922022" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-01-02&dno=128922022&filename=supremecourt/2022/12892/12892_2022_8_1501_40677_Judgement_02-Jan-2023.pdf target="_blank">2023 INSC 1 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>DEEPAK GABA</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>STATE OF UTTAR PRADESH</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>SYED JAFAR ALAM</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE SANJIV KHANNA, HON'BLE MR. JUSTICE M.M. SUNDRESH</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE SANJIV KHANNA</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  73</td>
                    <td>Diary Number</td>
                                            <td>13404 / 2008</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-006182-006183 / 2009</td>
                                        <td rowspan="5"><a href="/supremecourt/2008/13404/13404_2008_5_1501_41434_Judgement_02-Feb-2023.pdf" target="_blank"><a href=/supremecourt/2008/13404/13404_2008_5_1501_41434_Judgement_02-Feb-2023.pdf target="_blank">02-02-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2008/13404/13404_2008_5_1501_41434_Judgement_02-Feb-2023.pdf&dno=134042008" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-02-02&dno=134042008&filename=supremecourt/2008/13404/13404_2008_5_1501_41434_Judgement_02-Feb-2023.pdf target="_blank">2023 INSC 95 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>BAINI PRASAD (D) THR. LRS.</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>DURGA DEVI</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td> (MRS. ) VIPIN GUPTA</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td>RAJESH SRIVASTAVA</td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE AJAY RASTOGI, HON'BLE MR. JUSTICE C.T. RAVIKUMAR</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE AJAY RASTOGI</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  74</td>
                    <td>Diary Number</td>
                                            <td>13752 / 2018</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-000175-000175 / 2023</td>
                                        <td rowspan="5"><a href="/supremecourt/2018/13752/13752_2018_5_1501_40805_Judgement_09-Jan-2023.pdf" target="_blank"><a href=/supremecourt/2018/13752/13752_2018_5_1501_40805_Judgement_09-Jan-2023.pdf target="_blank">09-01-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2018/13752/13752_2018_5_1501_40805_Judgement_09-Jan-2023.pdf&dno=137522018" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-01-09&dno=137522018&filename=supremecourt/2018/13752/13752_2018_5_1501_40805_Judgement_09-Jan-2023.pdf target="_blank">2023 INSC 21 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>THE STATE BANK OF INDIA</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>KAMAL KISHORE PRASAD</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>SANJAY KAPUR</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE AJAY RASTOGI, HON'BLE MS. JUSTICE BELA M. TRIVEDI</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MS. JUSTICE BELA M. TRIVEDI</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  75</td>
                    <td>Diary Number</td>
                                            <td>14222 / 2008</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>Crl.A. No.-000987-000987 / 2009</td>
                                        <td rowspan="5"><a href="/supremecourt/2008/14222/14222_2008_3_1501_42431_Judgement_01-Mar-2023.pdf" target="_blank"><a href=/supremecourt/2008/14222/14222_2008_3_1501_42431_Judgement_01-Mar-2023.pdf target="_blank">01-03-2023 <strong>(English)</strong><br><a href=/supremecourt_vernacular/2008/14222/14222_2008_3_1501_42431_Judgement_01-Mar-2023_HIN.pdf target="_blank">01-03-2023 <strong>(हिन्दी)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2008/14222/14222_2008_3_1501_42431_Judgement_01-Mar-2023.pdf&dno=142222008" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-03-01&dno=142222008&filename=supremecourt/2008/14222/14222_2008_3_1501_42431_Judgement_01-Mar-2023.pdf target="_blank">2023 INSC 182 <strong>(English)</strong><br><a href=/pdfdate/index1.php?dt=2023-03-01&dno=142222008&filename=supremecourt_vernacular/2008/14222/14222_2008_3_1501_42431_Judgement_01-Mar-2023_HIN.pdf target="_blank">2023 INSC 182 <strong>(हिन्दी)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>RAVI DHINGRA</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>THE STATE OF HARYANA</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>KAMLENDRA MISHRA</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td>MONIKA GUSAIN</td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE K.M. JOSEPH, HON'BLE MRS. JUSTICE B.V. NAGARATHNA, HON'BLE MR. JUSTICE AHSANUDDIN AMANULLAH</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE K.M. JOSEPH</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  76</td>
                    <td>Diary Number</td>
                                            <td>14249 / 2013</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>Crl.A. No.-001904-001904 / 2014</td>
                                        <td rowspan="5"><a href="/supremecourt/2013/14249/14249_2013_13_1501_42257_Judgement_24-Feb-2023.pdf" target="_blank"><a href=/supremecourt/2013/14249/14249_2013_13_1501_42257_Judgement_24-Feb-2023.pdf target="_blank">24-02-2023 <strong>(English)</strong><br><a href=/supremecourt_vernacular/2013/14249/14249_2013_13_1501_42257_Judgement_24-Feb-2023_HIN.pdf target="_blank">24-02-2023 <strong>(हिन्दी)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2013/14249/14249_2013_13_1501_42257_Judgement_24-Feb-2023.pdf&dno=142492013" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-02-24&dno=142492013&filename=supremecourt/2013/14249/14249_2013_13_1501_42257_Judgement_24-Feb-2023.pdf target="_blank">2023 INSC 157 <strong>(English)</strong><br><a href=/pdfdate/index1.php?dt=2023-02-24&dno=142492013&filename=supremecourt_vernacular/2013/14249/14249_2013_13_1501_42257_Judgement_24-Feb-2023_HIN.pdf target="_blank">2023 INSC 157 <strong>(हिन्दी)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>ROOPWANTI</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>THE STATE OF HARYANA</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>SHIV KUMAR SURI</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td>MONIKA GUSAIN</td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE KRISHNA MURARI, HON'BLE MR. JUSTICE AHSANUDDIN AMANULLAH</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE KRISHNA MURARI</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  77</td>
                    <td>Diary Number</td>
                                            <td>14515 / 2022</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-001167-001170 / 2023</td>
                                        <td rowspan="5"><a href="/supremecourt/2022/14515/14515_2022_4_1508_42249_Judgement_24-Feb-2023.pdf" target="_blank"><a href=/supremecourt/2022/14515/14515_2022_4_1508_42249_Judgement_24-Feb-2023.pdf target="_blank">24-02-2023 <strong>(English)</strong><br><a href=/supremecourt_vernacular/2022/14515/14515_2022_4_1508_42249_Judgement_24-Feb-2023_TAM.pdf target="_blank">24-02-2023 <strong>(தமிழ்)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2022/14515/14515_2022_4_1508_42249_Judgement_24-Feb-2023.pdf&dno=145152022" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-02-24&dno=145152022&filename=supremecourt/2022/14515/14515_2022_4_1508_42249_Judgement_24-Feb-2023.pdf target="_blank">2023 INSC 161 <strong>(English)</strong><br><a href=/pdfdate/index1.php?dt=2023-02-24&dno=145152022&filename=supremecourt_vernacular/2022/14515/14515_2022_4_1508_42249_Judgement_24-Feb-2023_TAM.pdf target="_blank">2023 INSC 161 <strong>(தமிழ்)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>S. MURALI SUNDARAM</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>JOTHIBAI KANNAN</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>S. RAJAPPA</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH, HON'BLE MR. JUSTICE C.T. RAVIKUMAR</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  78</td>
                    <td>Diary Number</td>
                                            <td>14645 / 2022</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-001363-001364 / 2023</td>
                                        <td rowspan="5"><a href="/supremecourt/2022/14645/14645_2022_4_1509_42249_Judgement_24-Feb-2023.pdf" target="_blank"><a href=/supremecourt/2022/14645/14645_2022_4_1509_42249_Judgement_24-Feb-2023.pdf target="_blank">24-02-2023 <strong>(English)</strong><br><a href=/supremecourt_vernacular/2022/14645/14645_2022_4_1509_42249_Judgement_24-Feb-2023_TEL.pdf target="_blank">24-02-2023 <strong>(తెలుగు)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2022/14645/14645_2022_4_1509_42249_Judgement_24-Feb-2023.pdf&dno=146452022" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-02-24&dno=146452022&filename=supremecourt/2022/14645/14645_2022_4_1509_42249_Judgement_24-Feb-2023.pdf target="_blank">2023 INSC 162 <strong>(English)</strong><br><a href=/pdfdate/index1.php?dt=2023-02-24&dno=146452022&filename=supremecourt_vernacular/2022/14645/14645_2022_4_1509_42249_Judgement_24-Feb-2023_TEL.pdf target="_blank">2023 INSC 162 <strong>(తెలుగు)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>P. SHYAMALA</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>GUNDLUR MASTHAN</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>BIJOY KUMAR JAIN</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH, HON'BLE MR. JUSTICE C.T. RAVIKUMAR</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  79</td>
                    <td>Diary Number</td>
                                            <td>14927 / 2022</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>Crl.A. No.-000013-000013 / 2023</td>
                                        <td rowspan="5"><a href="/supremecourt/2022/14927/14927_2022_4_1513_42249_Judgement_24-Feb-2023.pdf" target="_blank"><a href=/supremecourt/2022/14927/14927_2022_4_1513_42249_Judgement_24-Feb-2023.pdf target="_blank">24-02-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2022/14927/14927_2022_4_1513_42249_Judgement_24-Feb-2023.pdf&dno=149272022" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-02-24&dno=149272022&filename=supremecourt/2022/14927/14927_2022_4_1513_42249_Judgement_24-Feb-2023.pdf target="_blank">2023 INSC 168 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>ANANT THANUR KARMUSE</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>STATE OF MAHARASHTRA</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>ASTHA PRASAD</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH, HON'BLE MR. JUSTICE C.T. RAVIKUMAR</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  80</td>
                    <td>Diary Number</td>
                                            <td>15121 / 2022</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>SLP(C) No.-010499 / 2022</td>
                                        <td rowspan="5"><a href="/supremecourt/2022/15121/15121_2022_5_1501_41000_Judgement_16-Jan-2023.pdf" target="_blank"><a href=/supremecourt/2022/15121/15121_2022_5_1501_41000_Judgement_16-Jan-2023.pdf target="_blank">16-01-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2022/15121/15121_2022_5_1501_41000_Judgement_16-Jan-2023.pdf&dno=151212022" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-01-16&dno=151212022&filename=supremecourt/2022/15121/15121_2022_5_1501_41000_Judgement_16-Jan-2023.pdf target="_blank">2023 INSC 42 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>EX CONST/ DVR MUKESH KUMAR RAIGAR</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>UNION OF INDIA</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>SYED MEHDI IMAM</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE AJAY RASTOGI, HON'BLE MS. JUSTICE BELA M. TRIVEDI</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE AJAY RASTOGI</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  81</td>
                    <td>Diary Number</td>
                                            <td>15374 / 2022</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-000337-000337 / 2023</td>
                                        <td rowspan="5"><a href="/supremecourt/2022/15374/15374_2022_4_1503_40999_Judgement_16-Jan-2023.pdf" target="_blank"><a href=/supremecourt/2022/15374/15374_2022_4_1503_40999_Judgement_16-Jan-2023.pdf target="_blank">16-01-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2022/15374/15374_2022_4_1503_40999_Judgement_16-Jan-2023.pdf&dno=153742022" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-01-16&dno=153742022&filename=supremecourt/2022/15374/15374_2022_4_1503_40999_Judgement_16-Jan-2023.pdf target="_blank">2023 INSC 43 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>DELHI DEVELOPMENT AUTHORITY</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>EMINENT MARKETING PVT. LTD.</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>NITIN MISHRA</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH, HON'BLE MR. JUSTICE C.T. RAVIKUMAR</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  82</td>
                    <td>Diary Number</td>
                                            <td>15564 / 2018</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-008819-008819 / 2022</td>
                                        <td rowspan="5"><a href="/supremecourt/2018/15564/15564_2018_13_1501_42025_Judgement_20-Feb-2023.pdf" target="_blank"><a href=/supremecourt/2018/15564/15564_2018_13_1501_42025_Judgement_20-Feb-2023.pdf target="_blank">20-02-2023 <strong>(English)</strong><br><a href=/supremecourt_vernacular/2018/15564/15564_2018_13_1501_42025_Judgement_20-Feb-2023_HIN.pdf target="_blank">20-02-2023 <strong>(हिन्दी)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2018/15564/15564_2018_13_1501_42025_Judgement_20-Feb-2023.pdf&dno=155642018" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-02-20&dno=155642018&filename=supremecourt/2018/15564/15564_2018_13_1501_42025_Judgement_20-Feb-2023.pdf target="_blank">2023 INSC 144 <strong>(English)</strong><br><a href=/pdfdate/index1.php?dt=2023-02-20&dno=155642018&filename=supremecourt_vernacular/2018/15564/15564_2018_13_1501_42025_Judgement_20-Feb-2023_HIN.pdf target="_blank">2023 INSC 144 <strong>(हिन्दी)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>RAMESH CHANDRA SHARMA</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>THE STATE OF UTTAR PRADESH</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>ROHIT KUMAR SINGH</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE KRISHNA MURARI, HON'BLE MR. JUSTICE AHSANUDDIN AMANULLAH</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE KRISHNA MURARI</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  83</td>
                    <td>Diary Number</td>
                                            <td>16233 / 2020</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-000859-000899 / 2023</td>
                                        <td rowspan="5"><a href="/supremecourt/2020/16233/16233_2020_4_1502_41739_Judgement_10-Feb-2023.pdf" target="_blank"><a href=/supremecourt/2020/16233/16233_2020_4_1502_41739_Judgement_10-Feb-2023.pdf target="_blank">10-02-2023 <strong>(English)</strong><br><a href=/supremecourt_vernacular/2020/16233/16233_2020_4_1502_41739_Judgement_10-Feb-2023_HIN.pdf target="_blank">10-02-2023 <strong>(हिन्दी)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2020/16233/16233_2020_4_1502_41739_Judgement_10-Feb-2023.pdf&dno=162332020" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-02-10&dno=162332020&filename=supremecourt/2020/16233/16233_2020_4_1502_41739_Judgement_10-Feb-2023.pdf target="_blank">2023 INSC 120 <strong>(English)</strong><br><a href=/pdfdate/index1.php?dt=2023-02-10&dno=162332020&filename=supremecourt_vernacular/2020/16233/16233_2020_4_1502_41739_Judgement_10-Feb-2023_HIN.pdf target="_blank">2023 INSC 120 <strong>(हिन्दी)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>THE STATE OF HARYANA</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>SUBHASH CHANDER</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>MONIKA GUSAIN</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH, HON'BLE MR. JUSTICE C.T. RAVIKUMAR</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  84</td>
                    <td>Diary Number</td>
                                            <td>16773 / 2022</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-000614-000614 / 2023</td>
                                        <td rowspan="5"><a href="/supremecourt/2022/16773/16773_2022_14_6_41407_Judgement_31-Jan-2023.pdf" target="_blank"><a href=/supremecourt/2022/16773/16773_2022_14_6_41407_Judgement_31-Jan-2023.pdf target="_blank">31-01-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2022/16773/16773_2022_14_6_41407_Judgement_31-Jan-2023.pdf&dno=167732022" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-01-31&dno=167732022&filename=supremecourt/2022/16773/16773_2022_14_6_41407_Judgement_31-Jan-2023.pdf target="_blank">2023 INSC 88 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>PR. COMMISSIONER OF INCOME TAX (EXEMPTIONS) DELHI</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>SERVANTS OF PEOPLE SOCIETY</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>RAJ BAHADUR YADAV</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE S. RAVINDRA BHAT, HON'BLE MR. JUSTICE DIPANKAR DATTA</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE S. RAVINDRA BHAT</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  85</td>
                    <td>Diary Number</td>
                                            <td>16890 / 2020</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-000916-000916 / 2023</td>
                                        <td rowspan="5"><a href="/supremecourt/2020/16890/16890_2020_11_1501_41637_Judgement_08-Feb-2023.pdf" target="_blank"><a href=/supremecourt/2020/16890/16890_2020_11_1501_41637_Judgement_08-Feb-2023.pdf target="_blank">08-02-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2020/16890/16890_2020_11_1501_41637_Judgement_08-Feb-2023.pdf&dno=168902020" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-02-08&dno=168902020&filename=supremecourt/2020/16890/16890_2020_11_1501_41637_Judgement_08-Feb-2023.pdf target="_blank">2023 INSC 105 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>VIBHUTI SHANKAR PANDEY</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>THE STATE OF MADHYA PRADESH</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>AJAY CHOUDHARY</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE ANIRUDDHA BOSE, HON'BLE MR. JUSTICE SUDHANSHU DHULIA</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE ANIRUDDHA BOSE</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  86</td>
                    <td>Diary Number</td>
                                            <td>17938 / 2022</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-000423-000423 / 2023</td>
                                        <td rowspan="5"><a href="/supremecourt/2022/17938/17938_2022_4_1511_41177_Judgement_20-Jan-2023.pdf" target="_blank"><a href=/supremecourt/2022/17938/17938_2022_4_1511_41177_Judgement_20-Jan-2023.pdf target="_blank">20-01-2023 <strong>(English)</strong><br><a href=/supremecourt_vernacular/2022/17938/17938_2022_4_1511_41177_Judgement_20-Jan-2023_HIN.pdf target="_blank">20-01-2023 <strong>(हिन्दी)</strong><br><a href=/supremecourt_vernacular/2022/17938/17938_2022_4_1511_41177_Judgement_20-Jan-2023_GUJ.pdf target="_blank">20-01-2023 <strong>(ગુજરાતી)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2022/17938/17938_2022_4_1511_41177_Judgement_20-Jan-2023.pdf&dno=179382022" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-01-20&dno=179382022&filename=supremecourt/2022/17938/17938_2022_4_1511_41177_Judgement_20-Jan-2023.pdf target="_blank">2023 INSC 71 <strong>(English)</strong><br><a href=/pdfdate/index1.php?dt=2023-01-20&dno=179382022&filename=supremecourt_vernacular/2022/17938/17938_2022_4_1511_41177_Judgement_20-Jan-2023_HIN.pdf target="_blank">2023 INSC 71 <strong>(हिन्दी)</strong><br><a href=/pdfdate/index1.php?dt=2023-01-20&dno=179382022&filename=supremecourt_vernacular/2022/17938/17938_2022_4_1511_41177_Judgement_20-Jan-2023_GUJ.pdf target="_blank">2023 INSC 71 <strong>(ગુજરાતી)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>DELHI DEVELOPMENT AUTHORITY</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>OM PRAKASH</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>MANIKA TRIPATHY</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH, HON'BLE MR. JUSTICE C.T. RAVIKUMAR</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  87</td>
                    <td>Diary Number</td>
                                            <td>18005 / 2021</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>W.P.(C) No.-000891 / 2021</td>
                                        <td rowspan="5"><a href="/supremecourt/2021/18005/18005_2021_12_1501_41507_Judgement_03-Feb-2023.pdf" target="_blank"><a href=/supremecourt/2021/18005/18005_2021_12_1501_41507_Judgement_03-Feb-2023.pdf target="_blank">03-02-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2021/18005/18005_2021_12_1501_41507_Judgement_03-Feb-2023.pdf&dno=180052021" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-02-03&dno=180052021&filename=supremecourt/2021/18005/18005_2021_12_1501_41507_Judgement_03-Feb-2023.pdf target="_blank">2023 INSC 99 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>ANUSHKA    RENGUNTHWAR</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>UNION OF INDIA</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>KUNAL CHEEMA</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE A.S. BOPANNA, HON'BLE MS. JUSTICE HIMA KOHLI</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE A.S. BOPANNA</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  88</td>
                    <td>Diary Number</td>
                                            <td>18175 / 2022</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>CONMT.PET.(C) No.-000352 / 2022</td>
                                        <td rowspan="5"><a href="/supremecourt/2022/18175/18175_2022_14_1502_41415_Judgement_02-Feb-2023.pdf" target="_blank"><a href=/supremecourt/2022/18175/18175_2022_14_1502_41415_Judgement_02-Feb-2023.pdf target="_blank">02-02-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2022/18175/18175_2022_14_1502_41415_Judgement_02-Feb-2023.pdf&dno=181752022" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-02-02&dno=181752022&filename=supremecourt/2022/18175/18175_2022_14_1502_41415_Judgement_02-Feb-2023.pdf target="_blank">2023 INSC 97 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>SNEHASIS GIRI</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>SUBHASIS MITRA</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>PULKIT AGARWAL</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE S. RAVINDRA BHAT, HON'BLE MR. JUSTICE DIPANKAR DATTA</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE S. RAVINDRA BHAT</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  89</td>
                    <td>Diary Number</td>
                                            <td>18199 / 2016</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-000619-000619 / 2023</td>
                                        <td rowspan="5"><a href="/supremecourt/2016/18199/18199_2016_4_1501_41739_Judgement_10-Feb-2023.pdf" target="_blank"><a href=/supremecourt/2016/18199/18199_2016_4_1501_41739_Judgement_10-Feb-2023.pdf target="_blank">10-02-2023 <strong>(English)</strong><br><a href=/supremecourt_vernacular/2016/18199/18199_2016_4_1501_41739_Judgement_10-Feb-2023_HIN.pdf target="_blank">10-02-2023 <strong>(हिन्दी)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2016/18199/18199_2016_4_1501_41739_Judgement_10-Feb-2023.pdf&dno=181992016" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-02-10&dno=181992016&filename=supremecourt/2016/18199/18199_2016_4_1501_41739_Judgement_10-Feb-2023.pdf target="_blank">2023 INSC 119 <strong>(English)</strong><br><a href=/pdfdate/index1.php?dt=2023-02-10&dno=181992016&filename=supremecourt_vernacular/2016/18199/18199_2016_4_1501_41739_Judgement_10-Feb-2023_HIN.pdf target="_blank">2023 INSC 119 <strong>(हिन्दी)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>GAS POINT PETROLEUM INDIA LIMITED</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>RAJENDRA MAROTHI</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>ARJUN GARG</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH, HON'BLE MR. JUSTICE C.T. RAVIKUMAR</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  90</td>
                    <td>Diary Number</td>
                                            <td>18281 / 2008</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-003504-003505 / 2010</td>
                                        <td rowspan="5"><a href="/supremecourt/2008/18281/18281_2008_2_1501_41720_Judgement_08-Feb-2023.pdf" target="_blank"><a href=/supremecourt/2008/18281/18281_2008_2_1501_41720_Judgement_08-Feb-2023.pdf target="_blank">08-02-2023 <strong>(English)</strong><br><a href=/supremecourt_vernacular/2008/18281/18281_2008_2_1501_41720_Judgement_08-Feb-2023_GUJ.pdf target="_blank">08-02-2023 <strong>(ગુજરાતી)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2008/18281/18281_2008_2_1501_41720_Judgement_08-Feb-2023.pdf&dno=182812008" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-02-08&dno=182812008&filename=supremecourt/2008/18281/18281_2008_2_1501_41720_Judgement_08-Feb-2023.pdf target="_blank">2023 INSC 103 <strong>(English)</strong><br><a href=/pdfdate/index1.php?dt=2023-02-08&dno=182812008&filename=supremecourt_vernacular/2008/18281/18281_2008_2_1501_41720_Judgement_08-Feb-2023_GUJ.pdf target="_blank">2023 INSC 103 <strong>(ગુજરાતી)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>M/S GAIL (INDIA )LTD</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>M/S.INDIAN PETROCHEM.CORP.LTD. THROUGH ITS MANAGER</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td> KHAITAN & CO.</td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE SANJAY KISHAN KAUL, HON'BLE MR. JUSTICE ABHAY S. OKA</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE SANJAY KISHAN KAUL</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  91</td>
                    <td>Diary Number</td>
                                            <td>18460 / 2009</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>Crl.A. No.-001384-001385 / 2009</td>
                                        <td rowspan="5"><a href="/supremecourt/2009/18460/18460_2009_8_106_40920_Judgement_12-Jan-2023.pdf" target="_blank"><a href=/supremecourt/2009/18460/18460_2009_8_106_40920_Judgement_12-Jan-2023.pdf target="_blank">12-01-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2009/18460/18460_2009_8_106_40920_Judgement_12-Jan-2023.pdf&dno=184602009" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-01-12&dno=184602009&filename=supremecourt/2009/18460/18460_2009_8_106_40920_Judgement_12-Jan-2023.pdf target="_blank">2023 INSC 25 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>RANVIR SINGH .</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>THE STATE OF MADHYA PRADESH</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>SHAKIL AHMED SYED</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td>C. D. SINGH</td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE B.R. GAVAI, HON'BLE MR. JUSTICE M.M. SUNDRESH</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE B.R. GAVAI</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  92</td>
                    <td>Diary Number</td>
                                            <td>18547 / 2022</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>Crl.A. No.-000256-000256 / 2023</td>
                                        <td rowspan="5"><a href="/supremecourt/2022/18547/18547_2022_4_1501_41358_Judgement_30-Jan-2023.pdf" target="_blank"><a href=/supremecourt/2022/18547/18547_2022_4_1501_41358_Judgement_30-Jan-2023.pdf target="_blank">30-01-2023 <strong>(English)</strong><br><a href=/supremecourt_vernacular/2022/18547/18547_2022_4_1501_41358_Judgement_30-Jan-2023_BEN.pdf target="_blank">30-01-2023 <strong>(বাংলা)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2022/18547/18547_2022_4_1501_41358_Judgement_30-Jan-2023.pdf&dno=185472022" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-01-30&dno=185472022&filename=supremecourt/2022/18547/18547_2022_4_1501_41358_Judgement_30-Jan-2023.pdf target="_blank">2023 INSC 86 <strong>(English)</strong><br><a href=/pdfdate/index1.php?dt=2023-01-30&dno=185472022&filename=supremecourt_vernacular/2022/18547/18547_2022_4_1501_41358_Judgement_30-Jan-2023_BEN.pdf target="_blank">2023 INSC 86 <strong>(বাংলা)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>USHA CHAKRABORTY</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>STATE OF WEST BENGAL</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>RAVI SHARMA</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH, HON'BLE MR. JUSTICE C.T. RAVIKUMAR</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE C.T. RAVIKUMAR</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  93</td>
                    <td>Diary Number</td>
                                            <td>18749 / 2008</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-000969-000969 / 2023</td>
                                        <td rowspan="5"><a href="/supremecourt/2008/18749/18749_2008_2_1501_41823_Judgement_10-Feb-2023.pdf" target="_blank"><a href=/supremecourt/2008/18749/18749_2008_2_1501_41823_Judgement_10-Feb-2023.pdf target="_blank">10-02-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2008/18749/18749_2008_2_1501_41823_Judgement_10-Feb-2023.pdf&dno=187492008" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-02-10&dno=187492008&filename=supremecourt/2008/18749/18749_2008_2_1501_41823_Judgement_10-Feb-2023.pdf target="_blank">2023 INSC 116 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>BAR COUNCIL OF INDIA</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>BONNIE FOI LAW COLLEGE .</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>ARDHENDUMAULI KUMAR PRASAD</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td>B. K. SATIJA</td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE SANJAY KISHAN KAUL, HON'BLE MR. JUSTICE SANJIV KHANNA, HON'BLE MR. JUSTICE ABHAY S. OKA, HON'BLE MR. JUSTICE VIKRAM NATH, HON'BLE MR. JUSTICE J.K. MAHESHWARI</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE SANJAY KISHAN KAUL</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  94</td>
                    <td>Diary Number</td>
                                            <td>18754 / 2022</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-000312-000312 / 2023</td>
                                        <td rowspan="5"><a href="/supremecourt/2022/18754/18754_2022_4_1512_41177_Judgement_20-Jan-2023.pdf" target="_blank"><a href=/supremecourt/2022/18754/18754_2022_4_1512_41177_Judgement_20-Jan-2023.pdf target="_blank">20-01-2023 <strong>(English)</strong><br><a href=/supremecourt_vernacular/2022/18754/18754_2022_4_1512_41177_Judgement_20-Jan-2023_TEL.pdf target="_blank">20-01-2023 <strong>(తెలుగు)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2022/18754/18754_2022_4_1512_41177_Judgement_20-Jan-2023.pdf&dno=187542022" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-01-20&dno=187542022&filename=supremecourt/2022/18754/18754_2022_4_1512_41177_Judgement_20-Jan-2023.pdf target="_blank">2023 INSC 60 <strong>(English)</strong><br><a href=/pdfdate/index1.php?dt=2023-01-20&dno=187542022&filename=supremecourt_vernacular/2022/18754/18754_2022_4_1512_41177_Judgement_20-Jan-2023_TEL.pdf target="_blank">2023 INSC 60 <strong>(తెలుగు)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>THE ESI CORPORATION</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>M/S RADHIKA THEATRE</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>VAIBHAV MANU SRIVASTAVA</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH, HON'BLE MR. JUSTICE C.T. RAVIKUMAR</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  95</td>
                    <td>Diary Number</td>
                                            <td>19075 / 2009</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-000024-000024 / 2013</td>
                                        <td rowspan="5"><a href="/supremecourt/2009/19075/19075_2009_1_5_42308_Judgement_27-Feb-2023.pdf" target="_blank"><a href=/supremecourt/2009/19075/19075_2009_1_5_42308_Judgement_27-Feb-2023.pdf target="_blank">27-02-2023 <strong>(English)</strong><br><a href=/supremecourt_vernacular/2009/19075/19075_2009_1_5_42308_Judgement_27-Feb-2023_GUJ.pdf target="_blank">27-02-2023 <strong>(ગુજરાતી)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2009/19075/19075_2009_1_5_42308_Judgement_27-Feb-2023.pdf&dno=190752009" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-02-27&dno=190752009&filename=supremecourt/2009/19075/19075_2009_1_5_42308_Judgement_27-Feb-2023.pdf target="_blank">2023 INSC 171 <strong>(English)</strong><br><a href=/pdfdate/index1.php?dt=2023-02-27&dno=190752009&filename=supremecourt_vernacular/2009/19075/19075_2009_1_5_42308_Judgement_27-Feb-2023_GUJ.pdf target="_blank">2023 INSC 171 <strong>(ગુજરાતી)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>BHARTIBEN CHANDRAKANTBHAI THAKOR</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>THE STATE OF GUJARAT</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>NACHIKETA JOSHI</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE THE CHIEF JUSTICE, HON'BLE MR. JUSTICE PAMIDIGHANTAM SRI NARASIMHA, HON'BLE MR. JUSTICE J.B. PARDIWALA</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE THE CHIEF JUSTICE</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  96</td>
                    <td>Diary Number</td>
                                            <td>19197 / 2017</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-000386-000386 / 2023</td>
                                        <td rowspan="5"><a href="/supremecourt/2017/19197/19197_2017_15_1501_41078_Judgement_17-Jan-2023.pdf" target="_blank"><a href=/supremecourt/2017/19197/19197_2017_15_1501_41078_Judgement_17-Jan-2023.pdf target="_blank">17-01-2023 <strong>(English)</strong><br><a href=/supremecourt_vernacular/2017/19197/19197_2017_15_1501_41078_Judgement_17-Jan-2023_MAR.pdf target="_blank">17-01-2023 <strong>(मराठी)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2017/19197/19197_2017_15_1501_41078_Judgement_17-Jan-2023.pdf&dno=191972017" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-01-17&dno=191972017&filename=supremecourt/2017/19197/19197_2017_15_1501_41078_Judgement_17-Jan-2023.pdf target="_blank">2023 INSC 49 <strong>(English)</strong><br><a href=/pdfdate/index1.php?dt=2023-01-17&dno=191972017&filename=supremecourt_vernacular/2017/19197/19197_2017_15_1501_41078_Judgement_17-Jan-2023_MAR.pdf target="_blank">2023 INSC 49 <strong>(मराठी)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>SHRI RAM SHRIDHAR CHIMURKAR</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>UNION OF INDIA</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td> K. SARADA DEVI</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE V. RAMASUBRAMANIAN, HON'BLE MRS. JUSTICE B.V. NAGARATHNA</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MRS. JUSTICE B.V. NAGARATHNA</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  97</td>
                    <td>Diary Number</td>
                                            <td>19400 / 2022</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-001392-001392 / 2023</td>
                                        <td rowspan="5"><a href="/supremecourt/2022/19400/19400_2022_6_1501_42095_Judgement_23-Feb-2023.pdf" target="_blank"><a href=/supremecourt/2022/19400/19400_2022_6_1501_42095_Judgement_23-Feb-2023.pdf target="_blank">23-02-2023 <strong>(English)</strong><br><a href=/supremecourt_vernacular/2022/19400/19400_2022_6_1501_42095_Judgement_23-Feb-2023_TAM.pdf target="_blank">23-02-2023 <strong>(தமிழ்)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2022/19400/19400_2022_6_1501_42095_Judgement_23-Feb-2023.pdf&dno=194002022" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-02-23&dno=194002022&filename=supremecourt/2022/19400/19400_2022_6_1501_42095_Judgement_23-Feb-2023.pdf target="_blank">2023 INSC 156 <strong>(English)</strong><br><a href=/pdfdate/index1.php?dt=2023-02-23&dno=194002022&filename=supremecourt_vernacular/2022/19400/19400_2022_6_1501_42095_Judgement_23-Feb-2023_TAM.pdf target="_blank">2023 INSC 156 <strong>(தமிழ்)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>THIRU K. PALANISWAMY</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>M. SHANMUGAM</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>BALAJI SRINIVASAN</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE DINESH MAHESHWARI, HON'BLE MR. JUSTICE SANJAY KUMAR</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE DINESH MAHESHWARI</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  98</td>
                    <td>Diary Number</td>
                                            <td>19753 / 2021</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>Crl.A. No.-000534-000534 / 2023</td>
                                        <td rowspan="5"><a href="/supremecourt/2021/19753/19753_2021_4_1502_42249_Judgement_24-Feb-2023.pdf" target="_blank"><a href=/supremecourt/2021/19753/19753_2021_4_1502_42249_Judgement_24-Feb-2023.pdf target="_blank">24-02-2023 <strong>(English)</strong><br><a href=/supremecourt_vernacular/2021/19753/19753_2021_4_1502_42249_Judgement_24-Feb-2023_TEL.pdf target="_blank">24-02-2023 <strong>(తెలుగు)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2021/19753/19753_2021_4_1502_42249_Judgement_24-Feb-2023.pdf&dno=197532021" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-02-24&dno=197532021&filename=supremecourt/2021/19753/19753_2021_4_1502_42249_Judgement_24-Feb-2023.pdf target="_blank">2023 INSC 163 <strong>(English)</strong><br><a href=/pdfdate/index1.php?dt=2023-02-24&dno=197532021&filename=supremecourt_vernacular/2021/19753/19753_2021_4_1502_42249_Judgement_24-Feb-2023_TEL.pdf target="_blank">2023 INSC 163 <strong>(తెలుగు)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>DIRECTORATE OF ENFORCEMENT</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>M. GOPAL REDDY</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>MUKESH KUMAR MARORIA</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH, HON'BLE MR. JUSTICE C.T. RAVIKUMAR</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  99</td>
                    <td>Diary Number</td>
                                            <td>20050 / 2018</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>Crl.A. No.-000284-000284 / 2023</td>
                                        <td rowspan="5"><a href="/supremecourt/2018/20050/20050_2018_13_1501_41547_Judgement_01-Feb-2023.pdf" target="_blank"><a href=/supremecourt/2018/20050/20050_2018_13_1501_41547_Judgement_01-Feb-2023.pdf target="_blank">01-02-2023 <strong>(English)</strong><br><a href=/supremecourt_vernacular/2018/20050/20050_2018_13_1501_41547_Judgement_01-Feb-2023_TEL.pdf target="_blank">01-02-2023 <strong>(తెలుగు)</strong><br><a href=/supremecourt_vernacular/2018/20050/20050_2018_13_1501_41547_Judgement_01-Feb-2023_GUJ.pdf target="_blank">01-02-2023 <strong>(ગુજરાતી)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2018/20050/20050_2018_13_1501_41547_Judgement_01-Feb-2023.pdf&dno=200502018" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-02-01&dno=200502018&filename=supremecourt/2018/20050/20050_2018_13_1501_41547_Judgement_01-Feb-2023.pdf target="_blank">2023 INSC 93 <strong>(English)</strong><br><a href=/pdfdate/index1.php?dt=2023-02-01&dno=200502018&filename=supremecourt_vernacular/2018/20050/20050_2018_13_1501_41547_Judgement_01-Feb-2023_TEL.pdf target="_blank">2023 INSC 93 <strong>(తెలుగు)</strong><br><a href=/pdfdate/index1.php?dt=2023-02-01&dno=200502018&filename=supremecourt_vernacular/2018/20050/20050_2018_13_1501_41547_Judgement_01-Feb-2023_GUJ.pdf target="_blank">2023 INSC 93 <strong>(ગુજરાતી)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>B V SESHAIAH</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>THE STATE OF TELANGANA</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td> M. RAMBABU AND CO.</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE KRISHNA MURARI, HON'BLE MRS. JUSTICE B.V. NAGARATHNA</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE KRISHNA MURARI</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  100</td>
                    <td>Diary Number</td>
                                            <td>20128 / 2017</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>Crl.A. No.-000644-000644 / 2023</td>
                                        <td rowspan="5"><a href="/supremecourt/2017/20128/20128_2017_17_1501_42399_Judgement_01-Mar-2023.pdf" target="_blank"><a href=/supremecourt/2017/20128/20128_2017_17_1501_42399_Judgement_01-Mar-2023.pdf target="_blank">01-03-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2017/20128/20128_2017_17_1501_42399_Judgement_01-Mar-2023.pdf&dno=201282017" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-03-01&dno=201282017&filename=supremecourt/2017/20128/20128_2017_17_1501_42399_Judgement_01-Mar-2023.pdf target="_blank">2023 INSC 186 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>VIKAS RATHI</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>THE STATE OF UTTAR PRADESH</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>SARVAM RITAM KHARE</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE ABHAY S. OKA, HON'BLE MR. JUSTICE RAJESH BINDAL</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE ABHAY S. OKA</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  101</td>
                    <td>Diary Number</td>
                                            <td>20174 / 2020</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-003343 / 2020</td>
                                        <td rowspan="5"><a href="/supremecourt/2020/20174/20174_2020_14_3_41701_Judgement_09-Feb-2023.pdf" target="_blank"><a href=/supremecourt/2020/20174/20174_2020_14_3_41701_Judgement_09-Feb-2023.pdf target="_blank">09-02-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2020/20174/20174_2020_14_3_41701_Judgement_09-Feb-2023.pdf&dno=201742020" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-02-09&dno=201742020&filename=supremecourt/2020/20174/20174_2020_14_3_41701_Judgement_09-Feb-2023.pdf target="_blank">2023 INSC 114 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>DEBASHIS SINHA</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>M/S R.N.R ENTERPRISE</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>RAJ KISHOR CHOUDHARY</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE S. RAVINDRA BHAT, HON'BLE MR. JUSTICE DIPANKAR DATTA</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE S. RAVINDRA BHAT</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  102</td>
                    <td>Diary Number</td>
                                            <td>20227 / 2010</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>Crl.A. No.-000762-000762 / 2012</td>
                                        <td rowspan="5"><a href="/supremecourt/2010/20227/20227_2010_6_1501_42094_Judgement_22-Feb-2023.pdf" target="_blank"><a href=/supremecourt/2010/20227/20227_2010_6_1501_42094_Judgement_22-Feb-2023.pdf target="_blank">22-02-2023 <strong>(English)</strong><br><a href=/supremecourt_vernacular/2010/20227/20227_2010_6_1501_42094_Judgement_22-Feb-2023_TAM.pdf target="_blank">22-02-2023 <strong>(தமிழ்)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2010/20227/20227_2010_6_1501_42094_Judgement_22-Feb-2023.pdf&dno=202272010" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-02-22&dno=202272010&filename=supremecourt/2010/20227/20227_2010_6_1501_42094_Judgement_22-Feb-2023.pdf target="_blank">2023 INSC 151 <strong>(English)</strong><br><a href=/pdfdate/index1.php?dt=2023-02-22&dno=202272010&filename=supremecourt_vernacular/2010/20227/20227_2010_6_1501_42094_Judgement_22-Feb-2023_TAM.pdf target="_blank">2023 INSC 151 <strong>(தமிழ்)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>VAHITHA</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>THE STATE OF TAMIL NADU</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>CHANCHAL KUMAR GANGULI</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td>JOSEPH ARISTOTLE S.</td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE DINESH MAHESHWARI, HON'BLE MR. JUSTICE SANJAY KUMAR</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE DINESH MAHESHWARI</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  103</td>
                    <td>Diary Number</td>
                                            <td>20603 / 2021</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>Crl.A. No.-000276-000278 / 2022</td>
                                        <td rowspan="5"><a href="/supremecourt/2021/20603/20603_2021_7_8_42195_Judgement_22-Feb-2023.pdf" target="_blank"><a href=/supremecourt/2021/20603/20603_2021_7_8_42195_Judgement_22-Feb-2023.pdf target="_blank">22-02-2023 <strong>(English)</strong><br><a href=/supremecourt_vernacular/2021/20603/20603_2021_7_8_42195_Judgement_22-Feb-2023_HIN.pdf target="_blank">22-02-2023 <strong>(हिन्दी)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2021/20603/20603_2021_7_8_42195_Judgement_22-Feb-2023.pdf&dno=206032021" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-02-22&dno=206032021&filename=supremecourt/2021/20603/20603_2021_7_8_42195_Judgement_22-Feb-2023.pdf target="_blank">2023 INSC 153 <strong>(English)</strong><br><a href=/pdfdate/index1.php?dt=2023-02-22&dno=206032021&filename=supremecourt_vernacular/2021/20603/20603_2021_7_8_42195_Judgement_22-Feb-2023_HIN.pdf target="_blank">2023 INSC 153 <strong>(हिन्दी)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>JAGDISH</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>THE STATE OF RAJASTHAN</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>NARESH KUMAR</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE SANJIV KHANNA, HON'BLE MR. JUSTICE M.M. SUNDRESH</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE SANJIV KHANNA</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  104</td>
                    <td>Diary Number</td>
                                            <td>20622 / 2022</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-000100-000101 / 2023</td>
                                        <td rowspan="5"><a href="/supremecourt/2022/20622/20622_2022_4_1504_41103_Judgement_19-Jan-2023.pdf" target="_blank"><a href=/supremecourt/2022/20622/20622_2022_4_1504_41103_Judgement_19-Jan-2023.pdf target="_blank">19-01-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2022/20622/20622_2022_4_1504_41103_Judgement_19-Jan-2023.pdf&dno=206222022" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-01-19&dno=206222022&filename=supremecourt/2022/20622/20622_2022_4_1504_41103_Judgement_19-Jan-2023.pdf target="_blank">2023 INSC 58 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>GAJANAND SHARMA</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>ADARSH SIKSHA PARISAD SAMITI</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>RUCHI KOHLI</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH, HON'BLE MS. JUSTICE HIMA KOHLI</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  105</td>
                    <td>Diary Number</td>
                                            <td>21240 / 2022</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>T.P.(C) No.-001621 / 2022</td>
                                        <td rowspan="5"><a href="/supremecourt/2022/21240/21240_2022_15_1501_41756_Judgement_10-Feb-2023.pdf" target="_blank"><a href=/supremecourt/2022/21240/21240_2022_15_1501_41756_Judgement_10-Feb-2023.pdf target="_blank">10-02-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2022/21240/21240_2022_15_1501_41756_Judgement_10-Feb-2023.pdf&dno=212402022" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-02-10&dno=212402022&filename=supremecourt/2022/21240/21240_2022_15_1501_41756_Judgement_10-Feb-2023.pdf target="_blank">2023 INSC 118 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>SEEMA KAUSHAL</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>DHEERAJ KUMAR</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>NITIN SALUJA</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE V. RAMASUBRAMANIAN, HON'BLE MR. JUSTICE PANKAJ MITHAL</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE V. RAMASUBRAMANIAN</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  106</td>
                    <td>Diary Number</td>
                                            <td>21296 / 2022</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-009287-009287 / 2022</td>
                                        <td rowspan="5"><a href="/supremecourt/2022/21296/21296_2022_4_1504_40999_Judgement_16-Jan-2023.pdf" target="_blank"><a href=/supremecourt/2022/21296/21296_2022_4_1504_40999_Judgement_16-Jan-2023.pdf target="_blank">16-01-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2022/21296/21296_2022_4_1504_40999_Judgement_16-Jan-2023.pdf&dno=212962022" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-01-16&dno=212962022&filename=supremecourt/2022/21296/21296_2022_4_1504_40999_Judgement_16-Jan-2023.pdf target="_blank">2023 INSC 47 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>DELHI DEVELOPMENT AUTHORITY</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>BEENA GUPTA (D) THROUGH LRS.</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>MALVIKA KAPILA</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH, HON'BLE MR. JUSTICE C.T. RAVIKUMAR</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  107</td>
                    <td>Diary Number</td>
                                            <td>21429 / 2012</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>Crl.A. No.-000598-000600 / 2013</td>
                                        <td rowspan="5"><a href="/supremecourt/2012/21429/21429_2012_8_1501_41863_Judgement_15-Feb-2023.pdf" target="_blank"><a href=/supremecourt/2012/21429/21429_2012_8_1501_41863_Judgement_15-Feb-2023.pdf target="_blank">15-02-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2012/21429/21429_2012_8_1501_41863_Judgement_15-Feb-2023.pdf&dno=214292012" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-02-15&dno=214292012&filename=supremecourt/2012/21429/21429_2012_8_1501_41863_Judgement_15-Feb-2023.pdf target="_blank">2023 INSC 127 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>AJAI ALIAS AJJU</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>THE STATE OF UTTAR PRADESH</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>NITIN KUMAR THAKUR</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE B.R. GAVAI, HON'BLE MR. JUSTICE VIKRAM NATH, HON'BLE MR. JUSTICE SANJAY KAROL</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE VIKRAM NATH</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  108</td>
                    <td>Diary Number</td>
                                            <td>21434 / 2006</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-000878-000878 / 2009</td>
                                        <td rowspan="5"><a href="/supremecourt/2006/21434/21434_2006_7_1501_40716_Judgement_04-Jan-2023.pdf" target="_blank"><a href=/supremecourt/2006/21434/21434_2006_7_1501_40716_Judgement_04-Jan-2023.pdf target="_blank">04-01-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2006/21434/21434_2006_7_1501_40716_Judgement_04-Jan-2023.pdf&dno=214342006" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-01-04&dno=214342006&filename=supremecourt/2006/21434/21434_2006_7_1501_40716_Judgement_04-Jan-2023.pdf target="_blank">2023 INSC 8 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>SMT. SMRITI DEBBARMA (D) THR LR.</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>SRI PRABHA RANJAN DEBBARMA</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>RAUF RAHIM</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td>KEDAR NATH TRIPATHY</td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE SANJIV KHANNA, HON'BLE MR. JUSTICE M.M. SUNDRESH</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE SANJIV KHANNA</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  109</td>
                    <td>Diary Number</td>
                                            <td>21674 / 2010</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-005981-005981 / 2014</td>
                                        <td rowspan="5"><a href="/supremecourt/2010/21674/21674_2010_2_109_42527_Judgement_01-Mar-2023.pdf" target="_blank"><a href=/supremecourt/2010/21674/21674_2010_2_109_42527_Judgement_01-Mar-2023.pdf target="_blank">01-03-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2010/21674/21674_2010_2_109_42527_Judgement_01-Mar-2023.pdf&dno=216742010" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-03-01&dno=216742010&filename=supremecourt/2010/21674/21674_2010_2_109_42527_Judgement_01-Mar-2023.pdf target="_blank">2023 INSC 185 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>SHANTI PRASAD (D) THR. LRS.</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>THAKUR DASS (D) THR. LRS.</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>DINESH KUMAR GARG</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE MANOJ MISRA, HON'BLE MR. JUSTICE ARAVIND KUMAR</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE MANOJ MISRA</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  110</td>
                    <td>Diary Number</td>
                                            <td>22033 / 2022</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-000472-000472 / 2023</td>
                                        <td rowspan="5"><a href="/supremecourt/2022/22033/22033_2022_4_1513_41177_Judgement_20-Jan-2023.pdf" target="_blank"><a href=/supremecourt/2022/22033/22033_2022_4_1513_41177_Judgement_20-Jan-2023.pdf target="_blank">20-01-2023 <strong>(English)</strong><br><a href=/supremecourt_vernacular/2022/22033/22033_2022_4_1513_41177_Judgement_20-Jan-2023_GUJ.pdf target="_blank">20-01-2023 <strong>(ગુજરાતી)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2022/22033/22033_2022_4_1513_41177_Judgement_20-Jan-2023.pdf&dno=220332022" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-01-20&dno=220332022&filename=supremecourt/2022/22033/22033_2022_4_1513_41177_Judgement_20-Jan-2023.pdf target="_blank">2023 INSC 61 <strong>(English)</strong><br><a href=/pdfdate/index1.php?dt=2023-01-20&dno=220332022&filename=supremecourt_vernacular/2022/22033/22033_2022_4_1513_41177_Judgement_20-Jan-2023_GUJ.pdf target="_blank">2023 INSC 61 <strong>(ગુજરાતી)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>MANUBHAI SENDHABHAI BHARWAD</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>OIL AND NATURAL GAS CORPORATION LTD.</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>JATIN ZAVERI</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH, HON'BLE MR. JUSTICE C.T. RAVIKUMAR</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  111</td>
                    <td>Diary Number</td>
                                            <td>22060 / 2022</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>Crl.A. No.-000037-000037 / 2023</td>
                                        <td rowspan="5"><a href="/supremecourt/2022/22060/22060_2022_4_1505_40999_Judgement_16-Jan-2023.pdf" target="_blank"><a href=/supremecourt/2022/22060/22060_2022_4_1505_40999_Judgement_16-Jan-2023.pdf target="_blank">16-01-2023 <strong>(English)</strong><br><a href=/supremecourt_vernacular/2022/22060/22060_2022_4_1505_40999_Judgement_16-Jan-2023_TEL.pdf target="_blank">16-01-2023 <strong>(తెలుగు)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2022/22060/22060_2022_4_1505_40999_Judgement_16-Jan-2023.pdf&dno=220602022" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-01-16&dno=220602022&filename=supremecourt/2022/22060/22060_2022_4_1505_40999_Judgement_16-Jan-2023.pdf target="_blank">2023 INSC 44 <strong>(English)</strong><br><a href=/pdfdate/index1.php?dt=2023-01-16&dno=220602022&filename=supremecourt_vernacular/2022/22060/22060_2022_4_1505_40999_Judgement_16-Jan-2023_TEL.pdf target="_blank">2023 INSC 44 <strong>(తెలుగు)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>THE STATE THROUGH CENTRAL BUREAU OF INVESTIGATION</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>T. GANGI REDDY @ YERRA GANGI REDDY</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>ARVIND KUMAR SHARMA</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH, HON'BLE MR. JUSTICE C.T. RAVIKUMAR</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  112</td>
                    <td>Diary Number</td>
                                            <td>22472 / 2022</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>T.P.(Crl.) No.-000526-000527 / 2022</td>
                                        <td rowspan="5"><a href="/supremecourt/2022/22472/22472_2022_6_1501_42075_Judgement_21-Feb-2023.pdf" target="_blank"><a href=/supremecourt/2022/22472/22472_2022_6_1501_42075_Judgement_21-Feb-2023.pdf target="_blank">21-02-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2022/22472/22472_2022_6_1501_42075_Judgement_21-Feb-2023.pdf&dno=224722022" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-02-21&dno=224722022&filename=supremecourt/2022/22472/22472_2022_6_1501_42075_Judgement_21-Feb-2023.pdf target="_blank">2023 INSC 150 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>YOGESH UPADHYAY</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>ATLANTA LIMITED</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>RAJEEV SINGH</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE DINESH MAHESHWARI, HON'BLE MR. JUSTICE SANJAY KUMAR</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE SANJAY KUMAR</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  113</td>
                    <td>Diary Number</td>
                                            <td>22491 / 2019</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-005373 / 2019</td>
                                        <td rowspan="5"><a href="/supremecourt/2019/22491/22491_2019_9_1501_41058_Judgement_17-Jan-2023.pdf" target="_blank"><a href=/supremecourt/2019/22491/22491_2019_9_1501_41058_Judgement_17-Jan-2023.pdf target="_blank">17-01-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2019/22491/22491_2019_9_1501_41058_Judgement_17-Jan-2023.pdf&dno=224912019" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-01-17&dno=224912019&filename=supremecourt/2019/22491/22491_2019_9_1501_41058_Judgement_17-Jan-2023.pdf target="_blank">2023 INSC 50 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>HEWLETT PACKARD INDIA SALES PVT.LTD.(NOW HP INDIA SALES PVT. LTD)</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>COMMISSIONER OF CUSTOMS (I) NHAVA SHEVA</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>CHARANYA LAKSHMIKUMARAN</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE SURYA KANT, HON'BLE MR. JUSTICE J.K. MAHESHWARI</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE SURYA KANT</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  114</td>
                    <td>Diary Number</td>
                                            <td>22629 / 2021</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-000360-000360 / 2023</td>
                                        <td rowspan="5"><a href="/supremecourt/2021/22629/22629_2021_4_1503_41177_Judgement_20-Jan-2023.pdf" target="_blank"><a href=/supremecourt/2021/22629/22629_2021_4_1503_41177_Judgement_20-Jan-2023.pdf target="_blank">20-01-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2021/22629/22629_2021_4_1503_41177_Judgement_20-Jan-2023.pdf&dno=226292021" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-01-20&dno=226292021&filename=supremecourt/2021/22629/22629_2021_4_1503_41177_Judgement_20-Jan-2023.pdf target="_blank">2023 INSC 64 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>GOVERNMENT OF NCT OF DELHI</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>MANJEET SINGH ANAND</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>ATUL KUMAR</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH, HON'BLE MR. JUSTICE C.T. RAVIKUMAR</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  115</td>
                    <td>Diary Number</td>
                                            <td>22952 / 2022</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-001312-001313 / 2023</td>
                                        <td rowspan="5"><a href="/supremecourt/2022/22952/22952_2022_14_1501_42082_Judgement_21-Feb-2023.pdf" target="_blank"><a href=/supremecourt/2022/22952/22952_2022_14_1501_42082_Judgement_21-Feb-2023.pdf target="_blank">21-02-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2022/22952/22952_2022_14_1501_42082_Judgement_21-Feb-2023.pdf&dno=229522022" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-02-21&dno=229522022&filename=supremecourt/2022/22952/22952_2022_14_1501_42082_Judgement_21-Feb-2023.pdf target="_blank">2023 INSC 149 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>SANWARLAL AGRAWAL</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>ASHOK KUMAR KOTHARI</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>UDAYADITYA BANERJEE</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE S. RAVINDRA BHAT, HON'BLE MR. JUSTICE DIPANKAR DATTA</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE S. RAVINDRA BHAT</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  116</td>
                    <td>Diary Number</td>
                                            <td>22998 / 2020</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>T.P.(C) No.-001249-001250 / 2020</td>
                                        <td rowspan="5"><a href="/supremecourt/2020/22998/22998_2020_1_31_40959_Judgement_13-Jan-2023.pdf" target="_blank"><a href=/supremecourt/2020/22998/22998_2020_1_31_40959_Judgement_13-Jan-2023.pdf target="_blank">13-01-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2020/22998/22998_2020_1_31_40959_Judgement_13-Jan-2023.pdf&dno=229982020" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-01-13&dno=229982020&filename=supremecourt/2020/22998/22998_2020_1_31_40959_Judgement_13-Jan-2023.pdf target="_blank">2023 INSC 35 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>ASHWINI KUMAR UPADHYAY</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>UNION OF INDIA</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>ASHWANI KUMAR DUBEY</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE THE CHIEF JUSTICE, HON'BLE MR. JUSTICE PAMIDIGHANTAM SRI NARASIMHA</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE THE CHIEF JUSTICE</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  117</td>
                    <td>Diary Number</td>
                                            <td>23204 / 2019</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>Crl.A. No.-000546-000546 / 2023</td>
                                        <td rowspan="5"><a href="/supremecourt/2019/23204/23204_2019_15_1503_42027_Judgement_20-Feb-2023.pdf" target="_blank"><a href=/supremecourt/2019/23204/23204_2019_15_1503_42027_Judgement_20-Feb-2023.pdf target="_blank">20-02-2023 <strong>(English)</strong><br><a href=/supremecourt_vernacular/2019/23204/23204_2019_15_1503_42027_Judgement_20-Feb-2023_HIN.pdf target="_blank">20-02-2023 <strong>(हिन्दी)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2019/23204/23204_2019_15_1503_42027_Judgement_20-Feb-2023.pdf&dno=232042019" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-02-20&dno=232042019&filename=supremecourt/2019/23204/23204_2019_15_1503_42027_Judgement_20-Feb-2023.pdf target="_blank">2023 INSC 143 <strong>(English)</strong><br><a href=/pdfdate/index1.php?dt=2023-02-20&dno=232042019&filename=supremecourt_vernacular/2019/23204/23204_2019_15_1503_42027_Judgement_20-Feb-2023_HIN.pdf target="_blank">2023 INSC 143 <strong>(हिन्दी)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>MITA INDIA PVT. LTD.</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>MAHENDRA JAIN</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>INDRA SAWHNEY</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE V. RAMASUBRAMANIAN, HON'BLE MR. JUSTICE PANKAJ MITHAL</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE V. RAMASUBRAMANIAN</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  118</td>
                    <td>Diary Number</td>
                                            <td>23260 / 2020</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-003626 / 2020</td>
                                        <td rowspan="5"><a href="/supremecourt/2020/23260/23260_2020_3_1501_41549_Judgement_01-Feb-2023.pdf" target="_blank"><a href=/supremecourt/2020/23260/23260_2020_3_1501_41549_Judgement_01-Feb-2023.pdf target="_blank">01-02-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2020/23260/23260_2020_3_1501_41549_Judgement_01-Feb-2023.pdf&dno=232602020" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-02-01&dno=232602020&filename=supremecourt/2020/23260/23260_2020_3_1501_41549_Judgement_01-Feb-2023.pdf target="_blank">2023 INSC 91 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>K.T.V. HEALTH FOOD PRIVATE LIMITED</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>UNION OF INDIA</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>MAYANK KSHIRSAGAR</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE K.M. JOSEPH, HON'BLE MR. JUSTICE AJAY RASTOGI, HON'BLE MR. JUSTICE ANIRUDDHA BOSE, HON'BLE MR. JUSTICE HRISHIKESH ROY, HON'BLE MR. JUSTICE C.T. RAVIKUMAR</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE K.M. JOSEPH</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  119</td>
                    <td>Diary Number</td>
                                            <td>23396 / 2022</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-000735-000735 / 2023</td>
                                        <td rowspan="5"><a href="/supremecourt/2022/23396/23396_2022_4_1505_41722_Judgement_09-Feb-2023.pdf" target="_blank"><a href=/supremecourt/2022/23396/23396_2022_4_1505_41722_Judgement_09-Feb-2023.pdf target="_blank">09-02-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2022/23396/23396_2022_4_1505_41722_Judgement_09-Feb-2023.pdf&dno=233962022" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-02-09&dno=233962022&filename=supremecourt/2022/23396/23396_2022_4_1505_41722_Judgement_09-Feb-2023.pdf target="_blank">2023 INSC 110 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>DELHI DEVELOPMENT AUTHORITY</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>NARVADA DEVI</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>MANIKA TRIPATHY</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH, HON'BLE MR. JUSTICE C.T. RAVIKUMAR, HON'BLE MR. JUSTICE SANJAY KAROL</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  120</td>
                    <td>Diary Number</td>
                                            <td>23515 / 2019</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-000220-000220 / 2023</td>
                                        <td rowspan="5"><a href="/supremecourt/2019/23515/23515_2019_4_1502_41177_Judgement_20-Jan-2023.pdf" target="_blank"><a href=/supremecourt/2019/23515/23515_2019_4_1502_41177_Judgement_20-Jan-2023.pdf target="_blank">20-01-2023 <strong>(English)</strong><br><a href=/supremecourt_vernacular/2019/23515/23515_2019_4_1502_41177_Judgement_20-Jan-2023_ORI.pdf target="_blank">20-01-2023 <strong>(ଓଡ଼ିଆ)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2019/23515/23515_2019_4_1502_41177_Judgement_20-Jan-2023.pdf&dno=235152019" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-01-20&dno=235152019&filename=supremecourt/2019/23515/23515_2019_4_1502_41177_Judgement_20-Jan-2023.pdf target="_blank">2023 INSC 63 <strong>(English)</strong><br><a href=/pdfdate/index1.php?dt=2023-01-20&dno=235152019&filename=supremecourt_vernacular/2019/23515/23515_2019_4_1502_41177_Judgement_20-Jan-2023_ORI.pdf target="_blank">2023 INSC 63 <strong>(ଓଡ଼ିଆ)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>MAHANADI COALFIELDS LTD</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>THE STATE OF ODISHA</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>SIDDHARTH JAIN </td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH, HON'BLE MR. JUSTICE C.T. RAVIKUMAR</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  121</td>
                    <td>Diary Number</td>
                                            <td>23980 / 2009</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>Crl.A. No.-002286-002286 / 2010</td>
                                        <td rowspan="5"><a href="/supremecourt/2009/23980/23980_2009_8_105_41087_Judgement_19-Jan-2023.pdf" target="_blank"><a href=/supremecourt/2009/23980/23980_2009_8_105_41087_Judgement_19-Jan-2023.pdf target="_blank">19-01-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2009/23980/23980_2009_8_105_41087_Judgement_19-Jan-2023.pdf&dno=239802009" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-01-19&dno=239802009&filename=supremecourt/2009/23980/23980_2009_8_105_41087_Judgement_19-Jan-2023.pdf target="_blank">2023 INSC 53 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>JASBIR SINGH</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>THE STATE OF PUNJAB</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>RAJIV MEHTA</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td>KARAN SHARMA</td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE B.R. GAVAI, HON'BLE MR. JUSTICE VIKRAM NATH</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE B.R. GAVAI</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  122</td>
                    <td>Diary Number</td>
                                            <td>24103 / 2022</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>Crl.A. No.-000205-000205 / 2023</td>
                                        <td rowspan="5"><a href="/supremecourt/2022/24103/24103_2022_2_6_41256_Judgement_24-Jan-2023.pdf" target="_blank"><a href=/supremecourt/2022/24103/24103_2022_2_6_41256_Judgement_24-Jan-2023.pdf target="_blank">24-01-2023 <strong>(English)</strong><br><a href=/supremecourt_vernacular/2022/24103/24103_2022_2_6_41256_Judgement_24-Jan-2023_HIN.pdf target="_blank">24-01-2023 <strong>(हिन्दी)</strong><br><a href=/supremecourt_vernacular/2022/24103/24103_2022_2_6_41256_Judgement_24-Jan-2023_GUJ.pdf target="_blank">24-01-2023 <strong>(ગુજરાતી)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2022/24103/24103_2022_2_6_41256_Judgement_24-Jan-2023.pdf&dno=241032022" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-01-24&dno=241032022&filename=supremecourt/2022/24103/24103_2022_2_6_41256_Judgement_24-Jan-2023.pdf target="_blank">2023 INSC 80 <strong>(English)</strong><br><a href=/pdfdate/index1.php?dt=2023-01-24&dno=241032022&filename=supremecourt_vernacular/2022/24103/24103_2022_2_6_41256_Judgement_24-Jan-2023_HIN.pdf target="_blank">2023 INSC 80 <strong>(हिन्दी)</strong><br><a href=/pdfdate/index1.php?dt=2023-01-24&dno=241032022&filename=supremecourt_vernacular/2022/24103/24103_2022_2_6_41256_Judgement_24-Jan-2023_GUJ.pdf target="_blank">2023 INSC 80 <strong>(ગુજરાતી)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>TALAT SANVI</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>STATE OF JHARKHAND</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>HIMANSHU BHUSHAN</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE SANJAY KISHAN KAUL, HON'BLE MR. JUSTICE ABHAY S. OKA</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE SANJAY KISHAN KAUL</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  123</td>
                    <td>Diary Number</td>
                                            <td>24369 / 2020</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>MA-002204 / 2020</td>
                                        <td rowspan="5"><a href="/supremecourt/2020/24369/24369_2020_3_501_41473_Judgement_31-Jan-2023.pdf" target="_blank"><a href=/supremecourt/2020/24369/24369_2020_3_501_41473_Judgement_31-Jan-2023.pdf target="_blank">31-01-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2020/24369/24369_2020_3_501_41473_Judgement_31-Jan-2023.pdf&dno=243692020" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-01-31&dno=243692020&filename=supremecourt/2020/24369/24369_2020_3_501_41473_Judgement_31-Jan-2023.pdf target="_blank">2023 INSC 87 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>JOSEPH SHINE</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>UNION OF INDIA SECRETARY</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>ARVIND KUMAR SHARMA</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE K.M. JOSEPH, HON'BLE MR. JUSTICE AJAY RASTOGI, HON'BLE MR. JUSTICE ANIRUDDHA BOSE, HON'BLE MR. JUSTICE HRISHIKESH ROY, HON'BLE MR. JUSTICE C.T. RAVIKUMAR</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE K.M. JOSEPH</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  124</td>
                    <td>Diary Number</td>
                                            <td>24437 / 2022</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-000944-000944 / 2023</td>
                                        <td rowspan="5"><a href="/supremecourt/2022/24437/24437_2022_4_1504_41935_Judgement_17-Feb-2023.pdf" target="_blank"><a href=/supremecourt/2022/24437/24437_2022_4_1504_41935_Judgement_17-Feb-2023.pdf target="_blank">17-02-2023 <strong>(English)</strong><br><a href=/supremecourt_vernacular/2022/24437/24437_2022_4_1504_41935_Judgement_17-Feb-2023_HIN.pdf target="_blank">17-02-2023 <strong>(हिन्दी)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2022/24437/24437_2022_4_1504_41935_Judgement_17-Feb-2023.pdf&dno=244372022" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-02-17&dno=244372022&filename=supremecourt/2022/24437/24437_2022_4_1504_41935_Judgement_17-Feb-2023.pdf target="_blank">2023 INSC 135 <strong>(English)</strong><br><a href=/pdfdate/index1.php?dt=2023-02-17&dno=244372022&filename=supremecourt_vernacular/2022/24437/24437_2022_4_1504_41935_Judgement_17-Feb-2023_HIN.pdf target="_blank">2023 INSC 135 <strong>(हिन्दी)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>DELHI DEVELOPMENT AUTHORITY</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>MGS (INDIA) PRIVATE LIMITED</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>NITIN MISHRA</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH, HON'BLE MR. JUSTICE C.T. RAVIKUMAR</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  125</td>
                    <td>Diary Number</td>
                                            <td>24828 / 2017</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>Crl.A. No.-000257-000257 / 2023</td>
                                        <td rowspan="5"><a href="/supremecourt/2017/24828/24828_2017_5_1501_41360_Judgement_30-Jan-2023.pdf" target="_blank"><a href=/supremecourt/2017/24828/24828_2017_5_1501_41360_Judgement_30-Jan-2023.pdf target="_blank">30-01-2023 <strong>(English)</strong><br><a href=/supremecourt_vernacular/2017/24828/24828_2017_5_1501_41360_Judgement_30-Jan-2023_HIN.pdf target="_blank">30-01-2023 <strong>(हिन्दी)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2017/24828/24828_2017_5_1501_41360_Judgement_30-Jan-2023.pdf&dno=248282017" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-01-30&dno=248282017&filename=supremecourt/2017/24828/24828_2017_5_1501_41360_Judgement_30-Jan-2023.pdf target="_blank">2023 INSC 85 <strong>(English)</strong><br><a href=/pdfdate/index1.php?dt=2023-01-30&dno=248282017&filename=supremecourt_vernacular/2017/24828/24828_2017_5_1501_41360_Judgement_30-Jan-2023_HIN.pdf target="_blank">2023 INSC 85 <strong>(हिन्दी)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>NAIM AHAMED</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>STATE (NCT OF DELHI)</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>RAJ KISHOR CHOUDHARY</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE AJAY RASTOGI, HON'BLE MS. JUSTICE BELA M. TRIVEDI</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MS. JUSTICE BELA M. TRIVEDI</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  126</td>
                    <td>Diary Number</td>
                                            <td>24886 / 2022</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-000379-000379 / 2023</td>
                                        <td rowspan="5"><a href="/supremecourt/2022/24886/24886_2022_4_1514_41177_Judgement_20-Jan-2023.pdf" target="_blank"><a href=/supremecourt/2022/24886/24886_2022_4_1514_41177_Judgement_20-Jan-2023.pdf target="_blank">20-01-2023 <strong>(English)</strong><br><a href=/supremecourt_vernacular/2022/24886/24886_2022_4_1514_41177_Judgement_20-Jan-2023_HIN.pdf target="_blank">20-01-2023 <strong>(हिन्दी)</strong><br><a href=/supremecourt_vernacular/2022/24886/24886_2022_4_1514_41177_Judgement_20-Jan-2023_GUJ.pdf target="_blank">20-01-2023 <strong>(ગુજરાતી)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2022/24886/24886_2022_4_1514_41177_Judgement_20-Jan-2023.pdf&dno=248862022" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-01-20&dno=248862022&filename=supremecourt/2022/24886/24886_2022_4_1514_41177_Judgement_20-Jan-2023.pdf target="_blank">2023 INSC 72 <strong>(English)</strong><br><a href=/pdfdate/index1.php?dt=2023-01-20&dno=248862022&filename=supremecourt_vernacular/2022/24886/24886_2022_4_1514_41177_Judgement_20-Jan-2023_HIN.pdf target="_blank">2023 INSC 72 <strong>(हिन्दी)</strong><br><a href=/pdfdate/index1.php?dt=2023-01-20&dno=248862022&filename=supremecourt_vernacular/2022/24886/24886_2022_4_1514_41177_Judgement_20-Jan-2023_GUJ.pdf target="_blank">2023 INSC 72 <strong>(ગુજરાતી)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>GOVERNMENT OF NCT OF DELHI</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>RATIRAM</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>CHANDRA PRAKASH</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH, HON'BLE MR. JUSTICE C.T. RAVIKUMAR</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  127</td>
                    <td>Diary Number</td>
                                            <td>25260 / 2021</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-006391 / 2021</td>
                                        <td rowspan="5"><a href="/supremecourt/2021/25260/25260_2021_8_1501_41569_Judgement_07-Feb-2023.pdf" target="_blank"><a href=/supremecourt/2021/25260/25260_2021_8_1501_41569_Judgement_07-Feb-2023.pdf target="_blank">07-02-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2021/25260/25260_2021_8_1501_41569_Judgement_07-Feb-2023.pdf&dno=252602021" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-02-07&dno=252602021&filename=supremecourt/2021/25260/25260_2021_8_1501_41569_Judgement_07-Feb-2023.pdf target="_blank">2023 INSC 100 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>ITC LIMITED</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>AASHNA ROY</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>DUA ASSOCIATES</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE B.R. GAVAI, HON'BLE MR. JUSTICE VIKRAM NATH</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE VIKRAM NATH</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  128</td>
                    <td>Diary Number</td>
                                            <td>25267 / 2022</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-000352-000352 / 2023</td>
                                        <td rowspan="5"><a href="/supremecourt/2022/25267/25267_2022_4_1503_41739_Judgement_10-Feb-2023.pdf" target="_blank"><a href=/supremecourt/2022/25267/25267_2022_4_1503_41739_Judgement_10-Feb-2023.pdf target="_blank">10-02-2023 <strong>(English)</strong><br><a href=/supremecourt_vernacular/2022/25267/25267_2022_4_1503_41739_Judgement_10-Feb-2023_HIN.pdf target="_blank">10-02-2023 <strong>(हिन्दी)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2022/25267/25267_2022_4_1503_41739_Judgement_10-Feb-2023.pdf&dno=252672022" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-02-10&dno=252672022&filename=supremecourt/2022/25267/25267_2022_4_1503_41739_Judgement_10-Feb-2023.pdf target="_blank">2023 INSC 121 <strong>(English)</strong><br><a href=/pdfdate/index1.php?dt=2023-02-10&dno=252672022&filename=supremecourt_vernacular/2022/25267/25267_2022_4_1503_41739_Judgement_10-Feb-2023_HIN.pdf target="_blank">2023 INSC 121 <strong>(हिन्दी)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>GOVT. OF NCT OF DELHI</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>SUSHIL KUMAR GUPTA</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>CHANDRA PRAKASH</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH, HON'BLE MR. JUSTICE C.T. RAVIKUMAR</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  129</td>
                    <td>Diary Number</td>
                                            <td>25347 / 2018</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-002965-002965 / 2022</td>
                                        <td rowspan="5"><a href="/supremecourt/2018/25347/25347_2018_4_1508_41047_Judgement_13-Jan-2023.pdf" target="_blank"><a href=/supremecourt/2018/25347/25347_2018_4_1508_41047_Judgement_13-Jan-2023.pdf target="_blank">13-01-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2018/25347/25347_2018_4_1508_41047_Judgement_13-Jan-2023.pdf&dno=253472018" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-01-13&dno=253472018&filename=supremecourt/2018/25347/25347_2018_4_1508_41047_Judgement_13-Jan-2023.pdf target="_blank">2023 INSC 34 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>MANIK MAJUMDER</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>DIPAK KUMAR SAHA (D) THR. LRS.</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>RAJAN K. CHOURASIA</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  130</td>
                    <td>Diary Number</td>
                                            <td>25360 / 2019</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>MA-001699 / 2019</td>
                                        <td rowspan="5"><a href="/supremecourt/2019/25360/25360_2019_3_504_41295_Judgement_24-Jan-2023.pdf" target="_blank"><a href=/supremecourt/2019/25360/25360_2019_3_504_41295_Judgement_24-Jan-2023.pdf target="_blank">24-01-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2019/25360/25360_2019_3_504_41295_Judgement_24-Jan-2023.pdf&dno=253602019" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-01-24&dno=253602019&filename=supremecourt/2019/25360/25360_2019_3_504_41295_Judgement_24-Jan-2023.pdf target="_blank">2023 INSC 77 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>COMMON CAUSE (A REGD. SOCIETY) DIRECTOR SH. H.D. SHOURIE</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>UNION OF INDIA (A) MINISTRY OF HEALTH AND FAMILY WELFARE SECRETARY</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>RASHMI NANDAKUMAR</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE K.M. JOSEPH, HON'BLE MR. JUSTICE AJAY RASTOGI, HON'BLE MR. JUSTICE ANIRUDDHA BOSE, HON'BLE MR. JUSTICE HRISHIKESH ROY, HON'BLE MR. JUSTICE C.T. RAVIKUMAR</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE K.M. JOSEPH</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  131</td>
                    <td>Diary Number</td>
                                            <td>25435 / 2022</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>W.P.(Crl.) No.-000323 / 2022</td>
                                        <td rowspan="5"><a href="/supremecourt/2022/25435/25435_2022_13_1501_41101_Judgement_13-Jan-2023.pdf" target="_blank"><a href=/supremecourt/2022/25435/25435_2022_13_1501_41101_Judgement_13-Jan-2023.pdf target="_blank">13-01-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2022/25435/25435_2022_13_1501_41101_Judgement_13-Jan-2023.pdf&dno=254352022" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-01-13&dno=254352022&filename=supremecourt/2022/25435/25435_2022_13_1501_41101_Judgement_13-Jan-2023.pdf target="_blank">2023 INSC 31 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>JASWANT SINGH</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>THE STATE OF CHHATTISGARH</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>MOHD. IRSHAD HANIF</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE VIKRAM NATH, HON'BLE MS. JUSTICE BELA M. TRIVEDI</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE VIKRAM NATH</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  132</td>
                    <td>Diary Number</td>
                                            <td>25723 / 2020</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>SLP(C) No.-000678 / 2021</td>
                                        <td rowspan="5"><a href="/supremecourt/2020/25723/25723_2020_5_1501_42385_Judgement_28-Feb-2023.pdf" target="_blank"><a href=/supremecourt/2020/25723/25723_2020_5_1501_42385_Judgement_28-Feb-2023.pdf target="_blank">28-02-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2020/25723/25723_2020_5_1501_42385_Judgement_28-Feb-2023.pdf&dno=257232020" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-02-28&dno=257232020&filename=supremecourt/2020/25723/25723_2020_5_1501_42385_Judgement_28-Feb-2023.pdf target="_blank">2023 INSC 179 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>IMTIYAZ AHMAD MALLA</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>THE STATE OF JAMMU AND KASHMIR</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>VIKRAM HEGDE</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE AJAY RASTOGI, HON'BLE MS. JUSTICE BELA M. TRIVEDI</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MS. JUSTICE BELA M. TRIVEDI</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  133</td>
                    <td>Diary Number</td>
                                            <td>25773 / 2022</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-001360-001360 / 2023</td>
                                        <td rowspan="5"><a href="/supremecourt/2022/25773/25773_2022_4_1510_42249_Judgement_24-Feb-2023.pdf" target="_blank"><a href=/supremecourt/2022/25773/25773_2022_4_1510_42249_Judgement_24-Feb-2023.pdf target="_blank">24-02-2023 <strong>(English)</strong><br><a href=/supremecourt_vernacular/2022/25773/25773_2022_4_1510_42249_Judgement_24-Feb-2023_HIN.pdf target="_blank">24-02-2023 <strong>(हिन्दी)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2022/25773/25773_2022_4_1510_42249_Judgement_24-Feb-2023.pdf&dno=257732022" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-02-24&dno=257732022&filename=supremecourt/2022/25773/25773_2022_4_1510_42249_Judgement_24-Feb-2023.pdf target="_blank">2023 INSC 169 <strong>(English)</strong><br><a href=/pdfdate/index1.php?dt=2023-02-24&dno=257732022&filename=supremecourt_vernacular/2022/25773/25773_2022_4_1510_42249_Judgement_24-Feb-2023_HIN.pdf target="_blank">2023 INSC 169 <strong>(हिन्दी)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>DELHI DEVELOPMENT AUTHORITY</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>AMIT JAIN</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>NITIN MISHRA</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH, HON'BLE MR. JUSTICE C.T. RAVIKUMAR</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  134</td>
                    <td>Diary Number</td>
                                            <td>26044 / 2021</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>W.P.(C) No.-001209 / 2021</td>
                                        <td rowspan="5"><a href="/supremecourt/2021/26044/26044_2021_4_1503_42249_Judgement_24-Feb-2023.pdf" target="_blank"><a href=/supremecourt/2021/26044/26044_2021_4_1503_42249_Judgement_24-Feb-2023.pdf target="_blank">24-02-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2021/26044/26044_2021_4_1503_42249_Judgement_24-Feb-2023.pdf&dno=260442021" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-02-24&dno=260442021&filename=supremecourt/2021/26044/26044_2021_4_1503_42249_Judgement_24-Feb-2023.pdf target="_blank">2023 INSC 164 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>R.K. JIBANLATA DEVI</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>HIGH COURT OF MANIPUR</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>RAJKUMARI BANJU</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH, HON'BLE MR. JUSTICE C.T. RAVIKUMAR</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  135</td>
                    <td>Diary Number</td>
                                            <td>26112 / 2020</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-007402-007402 / 2022</td>
                                        <td rowspan="5"><a href="/supremecourt/2020/26112/26112_2020_4_1502_40734_Judgement_05-Jan-2023.pdf" target="_blank"><a href=/supremecourt/2020/26112/26112_2020_4_1502_40734_Judgement_05-Jan-2023.pdf target="_blank">05-01-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2020/26112/26112_2020_4_1502_40734_Judgement_05-Jan-2023.pdf&dno=261122020" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-01-05&dno=261122020&filename=supremecourt/2020/26112/26112_2020_4_1502_40734_Judgement_05-Jan-2023.pdf target="_blank">2023 INSC 17 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>K. SREEDHAR</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>M/S RAUS CONSTRUCTIONS PVT. LTD.</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>TARUN GUPTA</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH, HON'BLE MR. JUSTICE C.T. RAVIKUMAR</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  136</td>
                    <td>Diary Number</td>
                                            <td>26470 / 2019</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>Crl.A. No.-001651-001651 / 2019</td>
                                        <td rowspan="5"><a href="/supremecourt/2019/26470/26470_2019_8_103_41087_Judgement_19-Jan-2023.pdf" target="_blank"><a href=/supremecourt/2019/26470/26470_2019_8_103_41087_Judgement_19-Jan-2023.pdf target="_blank">19-01-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2019/26470/26470_2019_8_103_41087_Judgement_19-Jan-2023.pdf&dno=264702019" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-01-19&dno=264702019&filename=supremecourt/2019/26470/26470_2019_8_103_41087_Judgement_19-Jan-2023.pdf target="_blank">2023 INSC 56 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>NATTHU SINGH</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>THE STATE OF UTTAR PRADESH</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>BIMAL ROY JAD</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE B.R. GAVAI, HON'BLE MR. JUSTICE VIKRAM NATH</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE B.R. GAVAI</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  137</td>
                    <td>Diary Number</td>
                                            <td>26479 / 2009</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>Crl.A. No.-001863-001863 / 2010</td>
                                        <td rowspan="5"><a href="/supremecourt/2009/26479/26479_2009_8_107_40920_Judgement_12-Jan-2023.pdf" target="_blank"><a href=/supremecourt/2009/26479/26479_2009_8_107_40920_Judgement_12-Jan-2023.pdf target="_blank">12-01-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2009/26479/26479_2009_8_107_40920_Judgement_12-Jan-2023.pdf&dno=264792009" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-01-12&dno=264792009&filename=supremecourt/2009/26479/26479_2009_8_107_40920_Judgement_12-Jan-2023.pdf target="_blank">2023 INSC 26 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>MOHINDER PAL</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>THE STATE OF JAMMU AND KASHMIR</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>DINESH KUMAR GARG</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE B.R. GAVAI, HON'BLE MR. JUSTICE M.M. SUNDRESH</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE B.R. GAVAI</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  138</td>
                    <td>Diary Number</td>
                                            <td>27041 / 2022</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>Crl.A. No.-002239-002240 / 2022</td>
                                        <td rowspan="5"><a href="/supremecourt/2022/27041/27041_2022_4_1504_40962_Judgement_13-Jan-2023.pdf" target="_blank"><a href=/supremecourt/2022/27041/27041_2022_4_1504_40962_Judgement_13-Jan-2023.pdf target="_blank">13-01-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2022/27041/27041_2022_4_1504_40962_Judgement_13-Jan-2023.pdf&dno=270412022" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-01-13&dno=270412022&filename=supremecourt/2022/27041/27041_2022_4_1504_40962_Judgement_13-Jan-2023.pdf target="_blank">2023 INSC 32 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>THE STATE OF RAJASTHAN</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>KOMAL LODHA</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>PRAGATI NEEKHRA</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH, HON'BLE MR. JUSTICE C.T. RAVIKUMAR</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  139</td>
                    <td>Diary Number</td>
                                            <td>27156 / 2016</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>W.P.(Crl.) No.-000113-000113 / 2016</td>
                                        <td rowspan="5"><a href="/supremecourt/2016/27156/27156_2016_3_1501_40744_Judgement_03-Jan-2023.pdf" target="_blank"><a href=/supremecourt/2016/27156/27156_2016_3_1501_40744_Judgement_03-Jan-2023.pdf target="_blank">03-01-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2016/27156/27156_2016_3_1501_40744_Judgement_03-Jan-2023.pdf&dno=271562016" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-01-03&dno=271562016&filename=supremecourt/2016/27156/27156_2016_3_1501_40744_Judgement_03-Jan-2023.pdf target="_blank">2023 INSC 4 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>KAUSHAL KISHOR</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>THE STATE OF UTTAR PRADESH GOVT. OF U.P. HOME SECRETARY</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>MANJU JETLEY</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE V. RAMASUBRAMANIAN</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  140</td>
                    <td>Diary Number</td>
                                            <td>27637 / 2022</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-001353-001353 / 2023</td>
                                        <td rowspan="5"><a href="/supremecourt/2022/27637/27637_2022_4_1511_42249_Judgement_24-Feb-2023.pdf" target="_blank"><a href=/supremecourt/2022/27637/27637_2022_4_1511_42249_Judgement_24-Feb-2023.pdf target="_blank">24-02-2023 <strong>(English)</strong><br><a href=/supremecourt_vernacular/2022/27637/27637_2022_4_1511_42249_Judgement_24-Feb-2023_HIN.pdf target="_blank">24-02-2023 <strong>(हिन्दी)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2022/27637/27637_2022_4_1511_42249_Judgement_24-Feb-2023.pdf&dno=276372022" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-02-24&dno=276372022&filename=supremecourt/2022/27637/27637_2022_4_1511_42249_Judgement_24-Feb-2023.pdf target="_blank">2023 INSC 170 <strong>(English)</strong><br><a href=/pdfdate/index1.php?dt=2023-02-24&dno=276372022&filename=supremecourt_vernacular/2022/27637/27637_2022_4_1511_42249_Judgement_24-Feb-2023_HIN.pdf target="_blank">2023 INSC 170 <strong>(हिन्दी)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>NATIONAL CAPITAL TERRITORY OF DELHI</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>SUBHASH CHANDER KHATRI</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>ATUL KUMAR</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH, HON'BLE MR. JUSTICE C.T. RAVIKUMAR</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  141</td>
                    <td>Diary Number</td>
                                            <td>27670 / 2008</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-010201-010202 / 2010</td>
                                        <td rowspan="5"><a href="/supremecourt/2008/27670/27670_2008_8_1501_40701_Judgement_03-Jan-2023.pdf" target="_blank"><a href=/supremecourt/2008/27670/27670_2008_8_1501_40701_Judgement_03-Jan-2023.pdf target="_blank">03-01-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2008/27670/27670_2008_8_1501_40701_Judgement_03-Jan-2023.pdf&dno=276702008" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-01-03&dno=276702008&filename=supremecourt/2008/27670/27670_2008_8_1501_40701_Judgement_03-Jan-2023.pdf target="_blank">2023 INSC 5 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>M/S.MUTHOOT LEASING AND FINANCE LTD. REP. BY ITS MANAGING DIRECTOR</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>THE COMMISSIONER OF INCOME TAX</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>E. M. S. ANAM</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE SANJIV KHANNA, HON'BLE MR. JUSTICE M.M. SUNDRESH</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE SANJIV KHANNA</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  142</td>
                    <td>Diary Number</td>
                                            <td>28000 / 2022</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-000945-000945 / 2023</td>
                                        <td rowspan="5"><a href="/supremecourt/2022/28000/28000_2022_4_1505_41935_Judgement_17-Feb-2023.pdf" target="_blank"><a href=/supremecourt/2022/28000/28000_2022_4_1505_41935_Judgement_17-Feb-2023.pdf target="_blank">17-02-2023 <strong>(English)</strong><br><a href=/supremecourt_vernacular/2022/28000/28000_2022_4_1505_41935_Judgement_17-Feb-2023_HIN.pdf target="_blank">17-02-2023 <strong>(हिन्दी)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2022/28000/28000_2022_4_1505_41935_Judgement_17-Feb-2023.pdf&dno=280002022" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-02-17&dno=280002022&filename=supremecourt/2022/28000/28000_2022_4_1505_41935_Judgement_17-Feb-2023.pdf target="_blank">2023 INSC 137 <strong>(English)</strong><br><a href=/pdfdate/index1.php?dt=2023-02-17&dno=280002022&filename=supremecourt_vernacular/2022/28000/28000_2022_4_1505_41935_Judgement_17-Feb-2023_HIN.pdf target="_blank">2023 INSC 137 <strong>(हिन्दी)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>LAND AND BUILDING DEPARTMENT</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>MANISH SETHI</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>ATUL KUMAR</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH, HON'BLE MR. JUSTICE C.T. RAVIKUMAR</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  143</td>
                    <td>Diary Number</td>
                                            <td>28193 / 2018</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-000077-000077 / 2023</td>
                                        <td rowspan="5"><a href="/supremecourt/2018/28193/28193_2018_1_42_40694_Judgement_03-Jan-2023.pdf" target="_blank"><a href=/supremecourt/2018/28193/28193_2018_1_42_40694_Judgement_03-Jan-2023.pdf target="_blank">03-01-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2018/28193/28193_2018_1_42_40694_Judgement_03-Jan-2023.pdf&dno=281932018" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-01-03&dno=281932018&filename=supremecourt/2018/28193/28193_2018_1_42_40694_Judgement_03-Jan-2023.pdf target="_blank">2023 INSC 6 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>K.C. CINEMA (CORRET NAME  K.C. THEATRE)</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>THE STATE OF JAMMU AND KASHMIR</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>ABHINAV SHRIVASTAVA</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE THE CHIEF JUSTICE, HON'BLE MR. JUSTICE PAMIDIGHANTAM SRI NARASIMHA</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE THE CHIEF JUSTICE</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  144</td>
                    <td>Diary Number</td>
                                            <td>28432 / 2022</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-000942-000942 / 2023</td>
                                        <td rowspan="5"><a href="/supremecourt/2022/28432/28432_2022_4_1506_41935_Judgement_17-Feb-2023.pdf" target="_blank"><a href=/supremecourt/2022/28432/28432_2022_4_1506_41935_Judgement_17-Feb-2023.pdf target="_blank">17-02-2023 <strong>(English)</strong><br><a href=/supremecourt_vernacular/2022/28432/28432_2022_4_1506_41935_Judgement_17-Feb-2023_HIN.pdf target="_blank">17-02-2023 <strong>(हिन्दी)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2022/28432/28432_2022_4_1506_41935_Judgement_17-Feb-2023.pdf&dno=284322022" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-02-17&dno=284322022&filename=supremecourt/2022/28432/28432_2022_4_1506_41935_Judgement_17-Feb-2023.pdf target="_blank">2023 INSC 138 <strong>(English)</strong><br><a href=/pdfdate/index1.php?dt=2023-02-17&dno=284322022&filename=supremecourt_vernacular/2022/28432/28432_2022_4_1506_41935_Judgement_17-Feb-2023_HIN.pdf target="_blank">2023 INSC 138 <strong>(हिन्दी)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>GOVT. OF NCT OF DELHI</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>DHANNU</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>ATUL KUMAR</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH, HON'BLE MR. JUSTICE C.T. RAVIKUMAR</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  145</td>
                    <td>Diary Number</td>
                                            <td>28438 / 2014</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-001838-001838 / 2018</td>
                                        <td rowspan="5"><a href="/supremecourt/2014/28438/28438_2014_11_1501_41005_Judgement_16-Jan-2023.pdf" target="_blank"><a href=/supremecourt/2014/28438/28438_2014_11_1501_41005_Judgement_16-Jan-2023.pdf target="_blank">16-01-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2014/28438/28438_2014_11_1501_41005_Judgement_16-Jan-2023.pdf&dno=284382014" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-01-16&dno=284382014&filename=supremecourt/2014/28438/28438_2014_11_1501_41005_Judgement_16-Jan-2023.pdf target="_blank">2023 INSC 40 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>SUSHIL PANDEY</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>THE STATE OF UTTAR PRADESH THR PRINCIPAL SECRETARY (HOME)</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>SRIDHAR POTARAJU</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE ANIRUDDHA BOSE, HON'BLE MR. JUSTICE SUDHANSHU DHULIA</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE ANIRUDDHA BOSE</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  146</td>
                    <td>Diary Number</td>
                                            <td>28748 / 2020</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>SLP(C) No.-018428-018584 / 2021</td>
                                        <td rowspan="5"><a href="/supremecourt/2020/28748/28748_2020_4_1502_41722_Judgement_09-Feb-2023.pdf" target="_blank"><a href=/supremecourt/2020/28748/28748_2020_4_1502_41722_Judgement_09-Feb-2023.pdf target="_blank">09-02-2023 <strong>(English)</strong><br><a href=/supremecourt_vernacular/2020/28748/28748_2020_4_1502_41722_Judgement_09-Feb-2023_HIN.pdf target="_blank">09-02-2023 <strong>(हिन्दी)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2020/28748/28748_2020_4_1502_41722_Judgement_09-Feb-2023.pdf&dno=287482020" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-02-09&dno=287482020&filename=supremecourt/2020/28748/28748_2020_4_1502_41722_Judgement_09-Feb-2023.pdf target="_blank">2023 INSC 113 <strong>(English)</strong><br><a href=/pdfdate/index1.php?dt=2023-02-09&dno=287482020&filename=supremecourt_vernacular/2020/28748/28748_2020_4_1502_41722_Judgement_09-Feb-2023_HIN.pdf target="_blank">2023 INSC 113 <strong>(हिन्दी)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>HARYANA STATE INDUSTRIAL AND INFRASTRUCTURE DEVELOPMENT CORPORATION LTD.</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>SATPAL</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>SAMAR VIJAY SINGH</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH, HON'BLE MR. JUSTICE C.T. RAVIKUMAR, HON'BLE MR. JUSTICE SANJAY KAROL</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  147</td>
                    <td>Diary Number</td>
                                            <td>28833 / 2021</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-000361-000361 / 2023</td>
                                        <td rowspan="5"><a href="/supremecourt/2021/28833/28833_2021_4_1504_41177_Judgement_20-Jan-2023.pdf" target="_blank"><a href=/supremecourt/2021/28833/28833_2021_4_1504_41177_Judgement_20-Jan-2023.pdf target="_blank">20-01-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2021/28833/28833_2021_4_1504_41177_Judgement_20-Jan-2023.pdf&dno=288332021" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-01-20&dno=288332021&filename=supremecourt/2021/28833/28833_2021_4_1504_41177_Judgement_20-Jan-2023.pdf target="_blank">2023 INSC 65 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>GOVERNMENT OF NCT OF DELHI</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>KHAJAN SINGH</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>SUJEETA SRIVASTAVA</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH, HON'BLE MR. JUSTICE C.T. RAVIKUMAR</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  148</td>
                    <td>Diary Number</td>
                                            <td>28925 / 2016</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-008550-008550 / 2022</td>
                                        <td rowspan="5"><a href="/supremecourt/2016/28925/28925_2016_1_1501_40959_Judgement_13-Jan-2023.pdf" target="_blank"><a href=/supremecourt/2016/28925/28925_2016_1_1501_40959_Judgement_13-Jan-2023.pdf target="_blank">13-01-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2016/28925/28925_2016_1_1501_40959_Judgement_13-Jan-2023.pdf&dno=289252016" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-01-13&dno=289252016&filename=supremecourt/2016/28925/28925_2016_1_1501_40959_Judgement_13-Jan-2023.pdf target="_blank">2023 INSC 33 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>THE CHIEF ENGINEER, WATER RESOURCES DEPARTMENT</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>RATTAN INDIA POWER LTD. THROUGH DIRECTOR</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE THE CHIEF JUSTICE, HON'BLE MR. JUSTICE PAMIDIGHANTAM SRI NARASIMHA</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE PAMIDIGHANTAM SRI NARASIMHA</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  149</td>
                    <td>Diary Number</td>
                                            <td>29159 / 2021</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-009205-009205 / 2022</td>
                                        <td rowspan="5"><a href="/supremecourt/2021/29159/29159_2021_4_1503_40962_Judgement_13-Jan-2023.pdf" target="_blank"><a href=/supremecourt/2021/29159/29159_2021_4_1503_40962_Judgement_13-Jan-2023.pdf target="_blank">13-01-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2021/29159/29159_2021_4_1503_40962_Judgement_13-Jan-2023.pdf&dno=291592021" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-01-13&dno=291592021&filename=supremecourt/2021/29159/29159_2021_4_1503_40962_Judgement_13-Jan-2023.pdf target="_blank">2023 INSC 36 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>THE STATE OF HARYANA</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>SUSHILA</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>MONIKA GUSAIN</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH, HON'BLE MR. JUSTICE C.T. RAVIKUMAR</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  150</td>
                    <td>Diary Number</td>
                                            <td>29444 / 2019</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>Crl.A. No.-002025-002025 / 2022</td>
                                        <td rowspan="5"><a href="/supremecourt/2019/29444/29444_2019_14_1501_41265_Judgement_24-Jan-2023.pdf" target="_blank"><a href=/supremecourt/2019/29444/29444_2019_14_1501_41265_Judgement_24-Jan-2023.pdf target="_blank">24-01-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2019/29444/29444_2019_14_1501_41265_Judgement_24-Jan-2023.pdf&dno=294442019" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-01-24&dno=294442019&filename=supremecourt/2019/29444/29444_2019_14_1501_41265_Judgement_24-Jan-2023.pdf target="_blank">2023 INSC 79 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>PRASAD PRADHAN</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>THE STATE OF CHHATTISGARH</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>JOGY SCARIA</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE S. RAVINDRA BHAT, HON'BLE MR. JUSTICE DIPANKAR DATTA</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE S. RAVINDRA BHAT</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  151</td>
                    <td>Diary Number</td>
                                            <td>29535 / 2022</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>SLP(Crl) No.-012574-012577 / 2022</td>
                                        <td rowspan="5"><a href="/supremecourt/2022/29535/29535_2022_4_1507_40734_Judgement_05-Jan-2023.pdf" target="_blank"><a href=/supremecourt/2022/29535/29535_2022_4_1507_40734_Judgement_05-Jan-2023.pdf target="_blank">05-01-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2022/29535/29535_2022_4_1507_40734_Judgement_05-Jan-2023.pdf&dno=295352022" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-01-05&dno=295352022&filename=supremecourt/2022/29535/29535_2022_4_1507_40734_Judgement_05-Jan-2023.pdf target="_blank">2023 INSC 16 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>ROHAN DHUNGAT</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>THE STATE OF GOA</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>SHIVRAJ GAONKAR</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH, HON'BLE MR. JUSTICE C.T. RAVIKUMAR</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  152</td>
                    <td>Diary Number</td>
                                            <td>29573 / 2022</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-000279-000279 / 2023</td>
                                        <td rowspan="5"><a href="/supremecourt/2022/29573/29573_2022_4_1505_40962_Judgement_13-Jan-2023.pdf" target="_blank"><a href=/supremecourt/2022/29573/29573_2022_4_1505_40962_Judgement_13-Jan-2023.pdf target="_blank">13-01-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2022/29573/29573_2022_4_1505_40962_Judgement_13-Jan-2023.pdf&dno=295732022" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-01-13&dno=295732022&filename=supremecourt/2022/29573/29573_2022_4_1505_40962_Judgement_13-Jan-2023.pdf target="_blank">2023 INSC 38 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>GOVT. OF NCT OF DELHI</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>BHAGRATI</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>ASTHA TYAGI</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH, HON'BLE MR. JUSTICE C.T. RAVIKUMAR</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  153</td>
                    <td>Diary Number</td>
                                            <td>29729 / 2017</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-006662-006662 / 2022</td>
                                        <td rowspan="5"><a href="/supremecourt/2017/29729/29729_2017_4_1501_40734_Judgement_05-Jan-2023.pdf" target="_blank"><a href=/supremecourt/2017/29729/29729_2017_4_1501_40734_Judgement_05-Jan-2023.pdf target="_blank">05-01-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2017/29729/29729_2017_4_1501_40734_Judgement_05-Jan-2023.pdf&dno=297292017" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-01-05&dno=297292017&filename=supremecourt/2017/29729/29729_2017_4_1501_40734_Judgement_05-Jan-2023.pdf target="_blank">2023 INSC 12 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>KOTAK MAHINDRA BANK LIMITED</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>GIRNAR CORRUGATORS PVT. LTD.</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>KRISHNAYAN SEN</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH, HON'BLE MR. JUSTICE C.T. RAVIKUMAR</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  154</td>
                    <td>Diary Number</td>
                                            <td>30157 / 2017</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>W.P.(C) No.-000940 / 2017</td>
                                        <td rowspan="5"><a href="/supremecourt/2017/30157/30157_2017_5_13_42385_Judgement_28-Feb-2023.pdf" target="_blank"><a href=/supremecourt/2017/30157/30157_2017_5_13_42385_Judgement_28-Feb-2023.pdf target="_blank">28-02-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2017/30157/30157_2017_5_13_42385_Judgement_28-Feb-2023.pdf&dno=301572017" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-02-28&dno=301572017&filename=supremecourt/2017/30157/30157_2017_5_13_42385_Judgement_28-Feb-2023.pdf target="_blank">2023 INSC 178 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>BIKRAM CHATTERJI</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>UNION OF INDIA</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>HIMANSHU SHEKHAR</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td>CYRIL AMARCHAND MANGALDAS AOR</td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE AJAY RASTOGI</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  155</td>
                    <td>Diary Number</td>
                                            <td>31201 / 2017</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>W.P.(C) No.-000967 / 2017</td>
                                        <td rowspan="5"><a href="/supremecourt/2017/31201/31201_2017_1_17_41449_Judgement_02-Feb-2023.pdf" target="_blank"><a href=/supremecourt/2017/31201/31201_2017_1_17_41449_Judgement_02-Feb-2023.pdf target="_blank">02-02-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2017/31201/31201_2017_1_17_41449_Judgement_02-Feb-2023.pdf&dno=312012017" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-02-02&dno=312012017&filename=supremecourt/2017/31201/31201_2017_1_17_41449_Judgement_02-Feb-2023.pdf target="_blank">2023 INSC 94 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>ASHWINI KUMAR UPADHYAY</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>UNION OF INDIA</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>R. D. UPADHYAY</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE THE CHIEF JUSTICE, HON'BLE MR. JUSTICE PAMIDIGHANTAM SRI NARASIMHA, HON'BLE MR. JUSTICE J.B. PARDIWALA</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE THE CHIEF JUSTICE</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  156</td>
                    <td>Diary Number</td>
                                            <td>31220 / 2018</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>SLP(Crl) No.-009221 / 2018</td>
                                        <td rowspan="5"><a href="/supremecourt/2018/31220/31220_2018_5_1501_41936_Judgement_17-Feb-2023.pdf" target="_blank"><a href=/supremecourt/2018/31220/31220_2018_5_1501_41936_Judgement_17-Feb-2023.pdf target="_blank">17-02-2023 <strong>(English)</strong><br><a href=/supremecourt_vernacular/2018/31220/31220_2018_9221_9221_2018_Judgement_17-Feb-2023_HIN.pdf target="_blank">17-02-2023 <strong>(हिन्दी)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2018/31220/31220_2018_5_1501_41936_Judgement_17-Feb-2023.pdf&dno=312202018" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-02-17&dno=312202018&filename=supremecourt/2018/31220/31220_2018_5_1501_41936_Judgement_17-Feb-2023.pdf target="_blank">2023 INSC 133 <strong>(English)</strong><br><a href=/pdfdate/index1.php?dt=2023-02-17&dno=312202018&filename=supremecourt_vernacular/2018/31220/31220_2018_9221_9221_2018_Judgement_17-Feb-2023_HIN.pdf target="_blank">2023 INSC 133 <strong>(हिन्दी)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>RAM GOPAL</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>THE STATE OF MADHYA PRADESH</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>SANJAY K. AGRAWAL</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE AJAY RASTOGI, HON'BLE MS. JUSTICE BELA M. TRIVEDI</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE AJAY RASTOGI</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  157</td>
                    <td>Diary Number</td>
                                            <td>31393 / 2007</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-005534-005594 / 2011</td>
                                        <td rowspan="5"><a href="/supremecourt/2007/31393/31393_2007_8_1501_40965_Judgement_13-Jan-2023.pdf" target="_blank"><a href=/supremecourt/2007/31393/31393_2007_8_1501_40965_Judgement_13-Jan-2023.pdf target="_blank">13-01-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2007/31393/31393_2007_8_1501_40965_Judgement_13-Jan-2023.pdf&dno=313932007" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-01-13&dno=313932007&filename=supremecourt/2007/31393/31393_2007_8_1501_40965_Judgement_13-Jan-2023.pdf target="_blank">2023 INSC 27 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>THE STATE OF HIMACHAL PRADESH</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>GOEL BUS SERVICE KULLU</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>ABHINAV MUKERJI</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE B.R. GAVAI, HON'BLE MR. JUSTICE VIKRAM NATH</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE VIKRAM NATH</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  158</td>
                    <td>Diary Number</td>
                                            <td>32553 / 2022</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-000943-000943 / 2023</td>
                                        <td rowspan="5"><a href="/supremecourt/2022/32553/32553_2022_4_1507_41935_Judgement_17-Feb-2023.pdf" target="_blank"><a href=/supremecourt/2022/32553/32553_2022_4_1507_41935_Judgement_17-Feb-2023.pdf target="_blank">17-02-2023 <strong>(English)</strong><br><a href=/supremecourt_vernacular/2022/32553/32553_2022_4_1507_41935_Judgement_17-Feb-2023_HIN.pdf target="_blank">17-02-2023 <strong>(हिन्दी)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2022/32553/32553_2022_4_1507_41935_Judgement_17-Feb-2023.pdf&dno=325532022" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-02-17&dno=325532022&filename=supremecourt/2022/32553/32553_2022_4_1507_41935_Judgement_17-Feb-2023.pdf target="_blank">2023 INSC 139 <strong>(English)</strong><br><a href=/pdfdate/index1.php?dt=2023-02-17&dno=325532022&filename=supremecourt_vernacular/2022/32553/32553_2022_4_1507_41935_Judgement_17-Feb-2023_HIN.pdf target="_blank">2023 INSC 139 <strong>(हिन्दी)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>DELHI DEVELOPMENT AUTHORITY</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>JAGAN SINGH</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>MANIKA TRIPATHY</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH, HON'BLE MR. JUSTICE C.T. RAVIKUMAR</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  159</td>
                    <td>Diary Number</td>
                                            <td>32601 / 2022</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-000280-000280 / 2023</td>
                                        <td rowspan="5"><a href="/supremecourt/2022/32601/32601_2022_4_1506_40962_Judgement_13-Jan-2023.pdf" target="_blank"><a href=/supremecourt/2022/32601/32601_2022_4_1506_40962_Judgement_13-Jan-2023.pdf target="_blank">13-01-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2022/32601/32601_2022_4_1506_40962_Judgement_13-Jan-2023.pdf&dno=326012022" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-01-13&dno=326012022&filename=supremecourt/2022/32601/32601_2022_4_1506_40962_Judgement_13-Jan-2023.pdf target="_blank">2023 INSC 39 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>GOVT. OF NCT OF DELHI</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>SUNIL JAIN</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>ASTHA TYAGI</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH, HON'BLE MR. JUSTICE C.T. RAVIKUMAR</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  160</td>
                    <td>Diary Number</td>
                                            <td>32640 / 2022</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-000395-000395 / 2023</td>
                                        <td rowspan="5"><a href="/supremecourt/2022/32640/32640_2022_4_1515_41177_Judgement_20-Jan-2023.pdf" target="_blank"><a href=/supremecourt/2022/32640/32640_2022_4_1515_41177_Judgement_20-Jan-2023.pdf target="_blank">20-01-2023 <strong>(English)</strong><br><a href=/supremecourt_vernacular/2022/32640/32640_2022_4_1515_41177_Judgement_20-Jan-2023_HIN.pdf target="_blank">20-01-2023 <strong>(हिन्दी)</strong><br><a href=/supremecourt_vernacular/2022/32640/32640_2022_4_1515_41177_Judgement_20-Jan-2023_GUJ.pdf target="_blank">20-01-2023 <strong>(ગુજરાતી)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2022/32640/32640_2022_4_1515_41177_Judgement_20-Jan-2023.pdf&dno=326402022" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-01-20&dno=326402022&filename=supremecourt/2022/32640/32640_2022_4_1515_41177_Judgement_20-Jan-2023.pdf target="_blank">2023 INSC 73 <strong>(English)</strong><br><a href=/pdfdate/index1.php?dt=2023-01-20&dno=326402022&filename=supremecourt_vernacular/2022/32640/32640_2022_4_1515_41177_Judgement_20-Jan-2023_HIN.pdf target="_blank">2023 INSC 73 <strong>(हिन्दी)</strong><br><a href=/pdfdate/index1.php?dt=2023-01-20&dno=326402022&filename=supremecourt_vernacular/2022/32640/32640_2022_4_1515_41177_Judgement_20-Jan-2023_GUJ.pdf target="_blank">2023 INSC 73 <strong>(ગુજરાતી)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>DELHI DEVELOPMENT AUTHORITY</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>NEM CHAND SHARMA</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>MALVIKA KAPILA</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH, HON'BLE MR. JUSTICE C.T. RAVIKUMAR</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  161</td>
                    <td>Diary Number</td>
                                            <td>32829 / 2014</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>Crl.A. No.-000490-000490 / 2017</td>
                                        <td rowspan="5"><a href="/supremecourt/2014/32829/32829_2014_14_1502_41265_Judgement_24-Jan-2023.pdf" target="_blank"><a href=/supremecourt/2014/32829/32829_2014_14_1502_41265_Judgement_24-Jan-2023.pdf target="_blank">24-01-2023 <strong>(English)</strong><br><a href=/supremecourt_vernacular/2014/32829/32829_2014_14_1502_41265_Judgement_24-Jan-2023_HIN.pdf target="_blank">24-01-2023 <strong>(हिन्दी)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2014/32829/32829_2014_14_1502_41265_Judgement_24-Jan-2023.pdf&dno=328292014" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-01-24&dno=328292014&filename=supremecourt/2014/32829/32829_2014_14_1502_41265_Judgement_24-Jan-2023.pdf target="_blank">2023 INSC 78 <strong>(English)</strong><br><a href=/pdfdate/index1.php?dt=2023-01-24&dno=328292014&filename=supremecourt_vernacular/2014/32829/32829_2014_14_1502_41265_Judgement_24-Jan-2023_HIN.pdf target="_blank">2023 INSC 78 <strong>(हिन्दी)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>MUNNA LAL</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>THE STATE OF UTTAR PRADESH</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>MUKESH K. GIRI</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE S. RAVINDRA BHAT, HON'BLE MR. JUSTICE DIPANKAR DATTA</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE DIPANKAR DATTA</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  162</td>
                    <td>Diary Number</td>
                                            <td>33696 / 2019</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-001491-001491 / 2023</td>
                                        <td rowspan="5"><a href="/supremecourt/2019/33696/33696_2019_6_1501_42313_Judgement_27-Feb-2023.pdf" target="_blank"><a href=/supremecourt/2019/33696/33696_2019_6_1501_42313_Judgement_27-Feb-2023.pdf target="_blank">27-02-2023 <strong>(English)</strong><br><a href=/supremecourt_vernacular/2019/33696/33696_2019_3_1491_1491_2019_Judgement_27-Feb-2023_MAL.pdf target="_blank">27-02-2023 <strong>(മലയാളം)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2019/33696/33696_2019_6_1501_42313_Judgement_27-Feb-2023.pdf&dno=336962019" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-02-27&dno=336962019&filename=supremecourt/2019/33696/33696_2019_6_1501_42313_Judgement_27-Feb-2023.pdf target="_blank">2023 INSC 173 <strong>(English)</strong><br><a href=/pdfdate/index1.php?dt=2023-02-27&dno=336962019&filename=supremecourt_vernacular/2019/33696/33696_2019_3_1491_1491_2019_Judgement_27-Feb-2023_MAL.pdf target="_blank">2023 INSC 173 <strong>(മലയാളം)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>SIRAJUDHEEN</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>ZEENATH</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>SRM LAW ASSOCIATES</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE DINESH MAHESHWARI, HON'BLE MR. JUSTICE SANJAY KUMAR</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE DINESH MAHESHWARI</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  163</td>
                    <td>Diary Number</td>
                                            <td>34090 / 2022</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-000397-000397 / 2023</td>
                                        <td rowspan="5"><a href="/supremecourt/2022/34090/34090_2022_4_1516_41177_Judgement_20-Jan-2023.pdf" target="_blank"><a href=/supremecourt/2022/34090/34090_2022_4_1516_41177_Judgement_20-Jan-2023.pdf target="_blank">20-01-2023 <strong>(English)</strong><br><a href=/supremecourt_vernacular/2022/34090/34090_2022_4_1516_41177_Judgement_20-Jan-2023_HIN.pdf target="_blank">20-01-2023 <strong>(हिन्दी)</strong><br><a href=/supremecourt_vernacular/2022/34090/34090_2022_4_1516_41177_Judgement_20-Jan-2023_GUJ.pdf target="_blank">20-01-2023 <strong>(ગુજરાતી)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2022/34090/34090_2022_4_1516_41177_Judgement_20-Jan-2023.pdf&dno=340902022" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-01-20&dno=340902022&filename=supremecourt/2022/34090/34090_2022_4_1516_41177_Judgement_20-Jan-2023.pdf target="_blank">2023 INSC 74 <strong>(English)</strong><br><a href=/pdfdate/index1.php?dt=2023-01-20&dno=340902022&filename=supremecourt_vernacular/2022/34090/34090_2022_4_1516_41177_Judgement_20-Jan-2023_HIN.pdf target="_blank">2023 INSC 74 <strong>(हिन्दी)</strong><br><a href=/pdfdate/index1.php?dt=2023-01-20&dno=340902022&filename=supremecourt_vernacular/2022/34090/34090_2022_4_1516_41177_Judgement_20-Jan-2023_GUJ.pdf target="_blank">2023 INSC 74 <strong>(ગુજરાતી)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>DELHI DEVELOPMENT AUTHORITY</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>DEWAN CHAND PRUTHI</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>MANIKA TRIPATHY</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH, HON'BLE MR. JUSTICE C.T. RAVIKUMAR</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  164</td>
                    <td>Diary Number</td>
                                            <td>34168 / 2009</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-008502-008502 / 2009</td>
                                        <td rowspan="5"><a href="/supremecourt/2009/34168/34168_2009_14_101_42417_Judgement_01-Mar-2023.pdf" target="_blank"><a href=/supremecourt/2009/34168/34168_2009_14_101_42417_Judgement_01-Mar-2023.pdf target="_blank">01-03-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2009/34168/34168_2009_14_101_42417_Judgement_01-Mar-2023.pdf&dno=341682009" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-03-01&dno=341682009&filename=supremecourt/2009/34168/34168_2009_14_101_42417_Judgement_01-Mar-2023.pdf target="_blank">2023 INSC 183 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>COMMR.OF CEN.EXC</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>M/S J.R. ORGANICS LTD.</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>MUKESH KUMAR MARORIA</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td>CHARANYA LAKSHMIKUMARAN</td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE S. RAVINDRA BHAT, HON'BLE MR. JUSTICE DIPANKAR DATTA</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE S. RAVINDRA BHAT</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  165</td>
                    <td>Diary Number</td>
                                            <td>34333 / 2022</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-000399-000399 / 2023</td>
                                        <td rowspan="5"><a href="/supremecourt/2022/34333/34333_2022_4_1517_41177_Judgement_20-Jan-2023.pdf" target="_blank"><a href=/supremecourt/2022/34333/34333_2022_4_1517_41177_Judgement_20-Jan-2023.pdf target="_blank">20-01-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2022/34333/34333_2022_4_1517_41177_Judgement_20-Jan-2023.pdf&dno=343332022" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-01-20&dno=343332022&filename=supremecourt/2022/34333/34333_2022_4_1517_41177_Judgement_20-Jan-2023.pdf target="_blank">2023 INSC 75 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>GOVT. OF NCT OF DELHI</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>RATI RAM</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>SUJEETA SRIVASTAVA</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH, HON'BLE MR. JUSTICE C.T. RAVIKUMAR</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  166</td>
                    <td>Diary Number</td>
                                            <td>34547 / 2022</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-000088-000089 / 2023</td>
                                        <td rowspan="5"><a href="/supremecourt/2022/34547/34547_2022_1_24_40710_Judgement_04-Jan-2023.pdf" target="_blank"><a href=/supremecourt/2022/34547/34547_2022_1_24_40710_Judgement_04-Jan-2023.pdf target="_blank">04-01-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2022/34547/34547_2022_1_24_40710_Judgement_04-Jan-2023.pdf&dno=345472022" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-01-04&dno=345472022&filename=supremecourt/2022/34547/34547_2022_1_24_40710_Judgement_04-Jan-2023.pdf target="_blank">2023 INSC 11 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>DEEPAK ANANDA PATIL</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>THE STATE OF MAHARASHTRA</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td> LAWYER S KNIT & CO</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE THE CHIEF JUSTICE, HON'BLE MR. JUSTICE S. ABDUL NAZEER, HON'BLE MR. JUSTICE PAMIDIGHANTAM SRI NARASIMHA</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE THE CHIEF JUSTICE</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  167</td>
                    <td>Diary Number</td>
                                            <td>34951 / 2015</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-000502-000503 / 2023</td>
                                        <td rowspan="5"><a href="/supremecourt/2015/34951/34951_2015_13_1501_41264_Judgement_24-Jan-2023.pdf" target="_blank"><a href=/supremecourt/2015/34951/34951_2015_13_1501_41264_Judgement_24-Jan-2023.pdf target="_blank">24-01-2023 <strong>(English)</strong><br><a href=/supremecourt_vernacular/2015/34951/34951_2015_13_1501_41264_Judgement_24-Jan-2023_ASM.pdf target="_blank">24-01-2023 <strong>(অসমীয়া)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2015/34951/34951_2015_13_1501_41264_Judgement_24-Jan-2023.pdf&dno=349512015" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-01-24&dno=349512015&filename=supremecourt/2015/34951/34951_2015_13_1501_41264_Judgement_24-Jan-2023.pdf target="_blank">2023 INSC 81 <strong>(English)</strong><br><a href=/pdfdate/index1.php?dt=2023-01-24&dno=349512015&filename=supremecourt_vernacular/2015/34951/34951_2015_13_1501_41264_Judgement_24-Jan-2023_ASM.pdf target="_blank">2023 INSC 81 <strong>(অসমীয়া)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>BAHARUL ISLAM .</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>THE INDIAN MEDICAL ASSOCIATION</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE KRISHNA MURARI, HON'BLE MRS. JUSTICE B.V. NAGARATHNA</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MRS. JUSTICE B.V. NAGARATHNA</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  168</td>
                    <td>Diary Number</td>
                                            <td>36547 / 2022</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-000765-000765 / 2023</td>
                                        <td rowspan="5"><a href="/supremecourt/2022/36547/36547_2022_6_13_41460_Judgement_02-Feb-2023.pdf" target="_blank"><a href=/supremecourt/2022/36547/36547_2022_6_13_41460_Judgement_02-Feb-2023.pdf target="_blank">02-02-2023 <strong>(English)</strong><br><a href=/supremecourt_vernacular/2022/36547/36547_2022_6_13_41460_Judgement_02-Feb-2023_HIN.pdf target="_blank">02-02-2023 <strong>(हिन्दी)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2022/36547/36547_2022_6_13_41460_Judgement_02-Feb-2023.pdf&dno=365472022" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-02-02&dno=365472022&filename=supremecourt/2022/36547/36547_2022_6_13_41460_Judgement_02-Feb-2023.pdf target="_blank">2023 INSC 98 <strong>(English)</strong><br><a href=/pdfdate/index1.php?dt=2023-02-02&dno=365472022&filename=supremecourt_vernacular/2022/36547/36547_2022_6_13_41460_Judgement_02-Feb-2023_HIN.pdf target="_blank">2023 INSC 98 <strong>(हिन्दी)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>SHYAM KUMAR GUPTA</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>SHUBHAM JAIN</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>PRATEEK KUMAR </td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE DINESH MAHESHWARI, HON'BLE MS. JUSTICE BELA M. TRIVEDI</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE DINESH MAHESHWARI</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  169</td>
                    <td>Diary Number</td>
                                            <td>36810 / 2019</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-000542-000542 / 2023</td>
                                        <td rowspan="5"><a href="/supremecourt/2019/36810/36810_2019_16_1501_42395_Judgement_28-Feb-2023.pdf" target="_blank"><a href=/supremecourt/2019/36810/36810_2019_16_1501_42395_Judgement_28-Feb-2023.pdf target="_blank">28-02-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2019/36810/36810_2019_16_1501_42395_Judgement_28-Feb-2023.pdf&dno=368102019" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-02-28&dno=368102019&filename=supremecourt/2019/36810/36810_2019_16_1501_42395_Judgement_28-Feb-2023.pdf target="_blank">2023 INSC 177 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>NATIONAL INSTITUTE OF RURAL DEVELOPMENT</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>SHYAM SUNDER PRASAD SHARMA</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE ABHAY S. OKA, HON'BLE MR. JUSTICE RAJESH BINDAL</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE ABHAY S. OKA</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  170</td>
                    <td>Diary Number</td>
                                            <td>36833 / 2018</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-002837-002837 / 2022</td>
                                        <td rowspan="5"><a href="/supremecourt/2018/36833/36833_2018_5_1501_42074_Judgement_21-Feb-2023.pdf" target="_blank"><a href=/supremecourt/2018/36833/36833_2018_5_1501_42074_Judgement_21-Feb-2023.pdf target="_blank">21-02-2023 <strong>(English)</strong><br><a href=/supremecourt_vernacular/2018/36833/36833_2018_5_1501_42074_Judgement_21-Feb-2023_GUJ.pdf target="_blank">21-02-2023 <strong>(ગુજરાતી)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2018/36833/36833_2018_5_1501_42074_Judgement_21-Feb-2023.pdf&dno=368332018" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-02-21&dno=368332018&filename=supremecourt/2018/36833/36833_2018_5_1501_42074_Judgement_21-Feb-2023.pdf target="_blank">2023 INSC 147 <strong>(English)</strong><br><a href=/pdfdate/index1.php?dt=2023-02-21&dno=368332018&filename=supremecourt_vernacular/2018/36833/36833_2018_5_1501_42074_Judgement_21-Feb-2023_GUJ.pdf target="_blank">2023 INSC 147 <strong>(ગુજરાતી)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>THE STATE OF GUJARAT</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>H B KAPADIA EDUCATION TRUST</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE AJAY RASTOGI, HON'BLE MS. JUSTICE BELA M. TRIVEDI</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE AJAY RASTOGI</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  171</td>
                    <td>Diary Number</td>
                                            <td>36848 / 2022</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-000946-000946 / 2023</td>
                                        <td rowspan="5"><a href="/supremecourt/2022/36848/36848_2022_4_1508_41935_Judgement_17-Feb-2023.pdf" target="_blank"><a href=/supremecourt/2022/36848/36848_2022_4_1508_41935_Judgement_17-Feb-2023.pdf target="_blank">17-02-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2022/36848/36848_2022_4_1508_41935_Judgement_17-Feb-2023.pdf&dno=368482022" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-02-17&dno=368482022&filename=supremecourt/2022/36848/36848_2022_4_1508_41935_Judgement_17-Feb-2023.pdf target="_blank">2023 INSC 140 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>GOVT. OF NCT OF DELHI</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>KRISHAN KUMAR</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>SUJEETA SRIVASTAVA</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH, HON'BLE MR. JUSTICE C.T. RAVIKUMAR</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  172</td>
                    <td>Diary Number</td>
                                            <td>36930 / 2009</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-008583-008584 / 2010</td>
                                        <td rowspan="5"><a href="/supremecourt/2009/36930/36930_2009_14_1501_41801_Judgement_09-Feb-2023.pdf" target="_blank"><a href=/supremecourt/2009/36930/36930_2009_14_1501_41801_Judgement_09-Feb-2023.pdf target="_blank">09-02-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2009/36930/36930_2009_14_1501_41801_Judgement_09-Feb-2023.pdf&dno=369302009" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-02-09&dno=369302009&filename=supremecourt/2009/36930/36930_2009_14_1501_41801_Judgement_09-Feb-2023.pdf target="_blank">2023 INSC 111 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>GTC INDUSTRIES LTD. (NOW KNOWN AS GOLDEN TOBACCO LIMITED) THROUGH MANAGER LEGAL</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>COLLECTOR OF CENTRAL EXCISE NEW DELHI</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>B. SUNITA RAO</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE S. RAVINDRA BHAT, HON'BLE MR. JUSTICE DIPANKAR DATTA</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE DIPANKAR DATTA</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  173</td>
                    <td>Diary Number</td>
                                            <td>37662 / 2016</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>W.P.(C) No.-000906-000906 / 2016</td>
                                        <td rowspan="5"><a href="/supremecourt/2016/37662/37662_2016_3_1501_40708_Judgement_02-Jan-2023.pdf" target="_blank"><a href=/supremecourt/2016/37662/37662_2016_3_1501_40708_Judgement_02-Jan-2023.pdf target="_blank">02-01-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2016/37662/37662_2016_3_1501_40708_Judgement_02-Jan-2023.pdf&dno=376622016" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-01-02&dno=376622016&filename=supremecourt/2016/37662/37662_2016_3_1501_40708_Judgement_02-Jan-2023.pdf target="_blank">2023 INSC 2 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>VIVEK NARAYAN SHARMA</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>UNION OF INDIA</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>PETITIONER-IN-PERSON</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td>ANIL KATIYAR</td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE B.R. GAVAI, HON'BLE MR. JUSTICE VIKRAM NATH</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE B.R. GAVAI</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  174</td>
                    <td>Diary Number</td>
                                            <td>37682 / 2010</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-003704-003704 / 2012</td>
                                        <td rowspan="5"><a href="/supremecourt/2010/37682/37682_2010_4_1501_40962_Judgement_13-Jan-2023.pdf" target="_blank"><a href=/supremecourt/2010/37682/37682_2010_4_1501_40962_Judgement_13-Jan-2023.pdf target="_blank">13-01-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2010/37682/37682_2010_4_1501_40962_Judgement_13-Jan-2023.pdf&dno=376822010" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-01-13&dno=376822010&filename=supremecourt/2010/37682/37682_2010_4_1501_40962_Judgement_13-Jan-2023.pdf target="_blank">2023 INSC 28 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>K.L. SWAMY</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>THE COMMISSIONER OF INCOME TAX</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>SENTHIL JAGADEESAN</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td>RAJ BAHADUR YADAV</td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH, HON'BLE MR. JUSTICE C.T. RAVIKUMAR</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  175</td>
                    <td>Diary Number</td>
                                            <td>37711 / 2012</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>Crl.A. No.-000972-000972 / 2013</td>
                                        <td rowspan="5"><a href="/supremecourt/2012/37711/37711_2012_14_1501_41061_Judgement_17-Jan-2023.pdf" target="_blank"><a href=/supremecourt/2012/37711/37711_2012_14_1501_41061_Judgement_17-Jan-2023.pdf target="_blank">17-01-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2012/37711/37711_2012_14_1501_41061_Judgement_17-Jan-2023.pdf&dno=377112012" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-01-17&dno=377112012&filename=supremecourt/2012/37711/37711_2012_14_1501_41061_Judgement_17-Jan-2023.pdf target="_blank">2023 INSC 48 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>JABIR</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>THE STATE OF UTTARAKHAND</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>VIKRANT SINGH BAIS</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE S. RAVINDRA BHAT, HON'BLE MR. JUSTICE DIPANKAR DATTA</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE S. RAVINDRA BHAT</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  176</td>
                    <td>Diary Number</td>
                                            <td>38587 / 2018</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-000778-000778 / 2023</td>
                                        <td rowspan="5"><a href="/supremecourt/2018/38587/38587_2018_14_1501_41415_Judgement_02-Feb-2023.pdf" target="_blank"><a href=/supremecourt/2018/38587/38587_2018_14_1501_41415_Judgement_02-Feb-2023.pdf target="_blank">02-02-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2018/38587/38587_2018_14_1501_41415_Judgement_02-Feb-2023.pdf&dno=385872018" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-02-02&dno=385872018&filename=supremecourt/2018/38587/38587_2018_14_1501_41415_Judgement_02-Feb-2023.pdf target="_blank">2023 INSC 96 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>MAHARASHTRA STATE FINANCIAL CORPORATION EXEMPLOYEES ASSOCIATION</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>THE STATE OF MAHARASHTRA</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>SESHATALPA SAI BANDARU</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE S. RAVINDRA BHAT, HON'BLE MR. JUSTICE DIPANKAR DATTA</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE S. RAVINDRA BHAT</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  177</td>
                    <td>Diary Number</td>
                                            <td>38687 / 2011</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-002627-002628 / 2012</td>
                                        <td rowspan="5"><a href="/supremecourt/2011/38687/38687_2011_5_1501_41810_Judgement_14-Feb-2023.pdf" target="_blank"><a href=/supremecourt/2011/38687/38687_2011_5_1501_41810_Judgement_14-Feb-2023.pdf target="_blank">14-02-2023 <strong>(English)</strong><br><a href=/supremecourt_vernacular/2011/38687/38687_2011_5_1501_41810_Judgement_14-Feb-2023_HIN.pdf target="_blank">14-02-2023 <strong>(हिन्दी)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2011/38687/38687_2011_5_1501_41810_Judgement_14-Feb-2023.pdf&dno=386872011" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-02-14&dno=386872011&filename=supremecourt/2011/38687/38687_2011_5_1501_41810_Judgement_14-Feb-2023.pdf target="_blank">2023 INSC 125 <strong>(English)</strong><br><a href=/pdfdate/index1.php?dt=2023-02-14&dno=386872011&filename=supremecourt_vernacular/2011/38687/38687_2011_5_1501_41810_Judgement_14-Feb-2023_HIN.pdf target="_blank">2023 INSC 125 <strong>(हिन्दी)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>KAMAL</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>GAJRAJ</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>ASHA GOPALAN NAIR</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td>BALRAJ DEWAN</td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE AJAY RASTOGI, HON'BLE MS. JUSTICE BELA M. TRIVEDI</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE AJAY RASTOGI</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  178</td>
                    <td>Diary Number</td>
                                            <td>39112 / 2010</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-008329-008329 / 2011</td>
                                        <td rowspan="5"><a href="/supremecourt/2010/39112/39112_2010_5_1501_42139_Judgement_22-Feb-2023.pdf" target="_blank"><a href=/supremecourt/2010/39112/39112_2010_5_1501_42139_Judgement_22-Feb-2023.pdf target="_blank">22-02-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2010/39112/39112_2010_5_1501_42139_Judgement_22-Feb-2023.pdf&dno=391122010" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-02-22&dno=391122010&filename=supremecourt/2010/39112/39112_2010_5_1501_42139_Judgement_22-Feb-2023.pdf target="_blank">2023 INSC 152 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>UNION OF INDIA</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>INDIAN NAVY CIVILIAN DESIGN OFFICERS ASSOCIATION THROUGH SHRI SWAPAN DEB</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>ARVIND KUMAR SHARMA</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td>EQUITY LEX ASSOCIATES</td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE AJAY RASTOGI, HON'BLE MS. JUSTICE BELA M. TRIVEDI</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MS. JUSTICE BELA M. TRIVEDI</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  179</td>
                    <td>Diary Number</td>
                                            <td>39129 / 2022</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>W.P.(C) No.-001126 / 2022</td>
                                        <td rowspan="5"><a href="/supremecourt/2022/39129/39129_2022_4_1518_41177_Judgement_20-Jan-2023.pdf" target="_blank"><a href=/supremecourt/2022/39129/39129_2022_4_1518_41177_Judgement_20-Jan-2023.pdf target="_blank">20-01-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2022/39129/39129_2022_4_1518_41177_Judgement_20-Jan-2023.pdf&dno=391292022" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-01-20&dno=391292022&filename=supremecourt/2022/39129/39129_2022_4_1518_41177_Judgement_20-Jan-2023.pdf target="_blank">2023 INSC 76 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>SAURAV DAS</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>UNION OF INDIA</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>PRASHANT BHUSHAN</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH, HON'BLE MR. JUSTICE C.T. RAVIKUMAR</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  180</td>
                    <td>Diary Number</td>
                                            <td>40192 / 2019</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-001141-001141 / 2023</td>
                                        <td rowspan="5"><a href="/supremecourt_vernacular/2019/40192/40192_2019_3_1141_1141_2019_Judgement_14-Feb-2023_HIN.pdf" target="_blank"><a href=/supremecourt_vernacular/2019/40192/40192_2019_3_1141_1141_2019_Judgement_14-Feb-2023_HIN.pdf target="_blank">14-02-2023 <strong>(हिन्दी)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt_vernacular/2019/40192/40192_2019_3_1141_1141_2019_Judgement_14-Feb-2023_HIN.pdf&dno=401922019" target="_blank"> </a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>DR. BR AMBEDKAR UNIVERSITY AGRA</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>DEVARSH NATH GUPTA</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>ASTHA SHARMA</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE DINESH MAHESHWARI, HON'BLE MR. JUSTICE SANJAY KUMAR</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td></td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  181</td>
                    <td>Diary Number</td>
                                            <td>40690 / 2018</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>Crl.A. No.-000001-000001 / 2023</td>
                                        <td rowspan="5"><a href="/supremecourt/2018/40690/40690_2018_7_1501_40729_Judgement_02-Jan-2023.pdf" target="_blank"><a href=/supremecourt/2018/40690/40690_2018_7_1501_40729_Judgement_02-Jan-2023.pdf target="_blank">02-01-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2018/40690/40690_2018_7_1501_40729_Judgement_02-Jan-2023.pdf&dno=406902018" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-01-02&dno=406902018&filename=supremecourt/2018/40690/40690_2018_7_1501_40729_Judgement_02-Jan-2023.pdf target="_blank">2023 INSC 3 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>PREM SINGH</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>STATE OF NCT DELHI</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>SHIV KUMAR SURI</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE DINESH MAHESHWARI, HON'BLE MR. JUSTICE SUDHANSHU DHULIA</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE DINESH MAHESHWARI</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  182</td>
                    <td>Diary Number</td>
                                            <td>40836 / 2019</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-000083-000083 / 2023</td>
                                        <td rowspan="5"><a href="/supremecourt/2019/40836/40836_2019_4_1502_40962_Judgement_13-Jan-2023.pdf" target="_blank"><a href=/supremecourt/2019/40836/40836_2019_4_1502_40962_Judgement_13-Jan-2023.pdf target="_blank">13-01-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2019/40836/40836_2019_4_1502_40962_Judgement_13-Jan-2023.pdf&dno=408362019" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-01-13&dno=408362019&filename=supremecourt/2019/40836/40836_2019_4_1502_40962_Judgement_13-Jan-2023.pdf target="_blank">2023 INSC 30 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>M/S OSWAL PLASTIC INDUSTRIES</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>MANAGER LEGAL DEPTT N.A.I.C.O LTD</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>DHANANJAY GARG</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH, HON'BLE MR. JUSTICE C.T. RAVIKUMAR</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  183</td>
                    <td>Diary Number</td>
                                            <td>41042 / 2017</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-004769-004769 / 2022</td>
                                        <td rowspan="5"><a href="/supremecourt/2017/41042/41042_2017_2_1502_41720_Judgement_08-Feb-2023.pdf" target="_blank"><a href=/supremecourt/2017/41042/41042_2017_2_1502_41720_Judgement_08-Feb-2023.pdf target="_blank">08-02-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2017/41042/41042_2017_2_1502_41720_Judgement_08-Feb-2023.pdf&dno=410422017" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-02-08&dno=410422017&filename=supremecourt/2017/41042/41042_2017_2_1502_41720_Judgement_08-Feb-2023.pdf target="_blank">2023 INSC 104 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>NATIONAL INSURANCE COMPANY LTD.</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>THE CHIEF ELECTORAL OFFICER</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>GARVESH KABRA</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE SANJAY KISHAN KAUL, HON'BLE MR. JUSTICE ABHAY S. OKA</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE SANJAY KISHAN KAUL</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  184</td>
                    <td>Diary Number</td>
                                            <td>41186 / 2022</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>SLP(Crl) No.-000834-000835 / 2023</td>
                                        <td rowspan="5"><a href="/supremecourt/2022/41186/41186_2022_6_33_41001_Judgement_16-Jan-2023.pdf" target="_blank"><a href=/supremecourt/2022/41186/41186_2022_6_33_41001_Judgement_16-Jan-2023.pdf target="_blank">16-01-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2022/41186/41186_2022_6_33_41001_Judgement_16-Jan-2023.pdf&dno=411862022" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-01-16&dno=411862022&filename=supremecourt/2022/41186/41186_2022_6_33_41001_Judgement_16-Jan-2023.pdf target="_blank">2023 INSC 45 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>BIMLA TIWARI</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>THE STATE OF BIHAR</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>SHAURYA SAHAY </td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE DINESH MAHESHWARI, HON'BLE MR. JUSTICE HRISHIKESH ROY</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE DINESH MAHESHWARI</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  185</td>
                    <td>Diary Number</td>
                                            <td>41540 / 2018</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-000277-000277 / 2023</td>
                                        <td rowspan="5"><a href="/supremecourt/2018/41540/41540_2018_4_1501_40999_Judgement_16-Jan-2023.pdf" target="_blank"><a href=/supremecourt/2018/41540/41540_2018_4_1501_40999_Judgement_16-Jan-2023.pdf target="_blank">16-01-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2018/41540/41540_2018_4_1501_40999_Judgement_16-Jan-2023.pdf&dno=415402018" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-01-16&dno=415402018&filename=supremecourt/2018/41540/41540_2018_4_1501_40999_Judgement_16-Jan-2023.pdf target="_blank">2023 INSC 46 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>DELHI DEVELOPMENT AUTHORITY</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>MANPREET SINGH</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>ASHWANI KUMAR</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH, HON'BLE MR. JUSTICE C.T. RAVIKUMAR</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE M.R. SHAH</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  186</td>
                    <td>Diary Number</td>
                                            <td>42359 / 2019</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>Crl.A. No.-000452-000452 / 2023</td>
                                        <td rowspan="5"><a href="/supremecourt/2019/42359/42359_2019_5_1502_41810_Judgement_14-Feb-2023.pdf" target="_blank"><a href=/supremecourt/2019/42359/42359_2019_5_1502_41810_Judgement_14-Feb-2023.pdf target="_blank">14-02-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2019/42359/42359_2019_5_1502_41810_Judgement_14-Feb-2023.pdf&dno=423592019" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-02-14&dno=423592019&filename=supremecourt/2019/42359/42359_2019_5_1502_41810_Judgement_14-Feb-2023.pdf target="_blank">2023 INSC 126 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>SURESH</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>THE STATE OF KERALA</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>SANGEETA KUMAR</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE AJAY RASTOGI, HON'BLE MS. JUSTICE BELA M. TRIVEDI</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE AJAY RASTOGI</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  187</td>
                    <td>Diary Number</td>
                                            <td>42527 / 2016</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-008726-008726 / 2018</td>
                                        <td rowspan="5"><a href="/supremecourt/2016/42527/42527_2016_5_1501_42017_Judgement_20-Feb-2023.pdf" target="_blank"><a href=/supremecourt/2016/42527/42527_2016_5_1501_42017_Judgement_20-Feb-2023.pdf target="_blank">20-02-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2016/42527/42527_2016_5_1501_42017_Judgement_20-Feb-2023.pdf&dno=425272016" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-02-20&dno=425272016&filename=supremecourt/2016/42527/42527_2016_5_1501_42017_Judgement_20-Feb-2023.pdf target="_blank">2023 INSC 141 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>SOUTH EASTERN COALFIELD LTD. AND ORS.</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>GULSHAN PRAKASH</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>ASHWARYA SINHA</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE MR. JUSTICE AJAY RASTOGI, HON'BLE MS. JUSTICE BELA M. TRIVEDI</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE AJAY RASTOGI</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  188</td>
                    <td>Diary Number</td>
                                            <td>43763 / 2019</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>MA-002680 / 2019</td>
                                        <td rowspan="5"><a href="/supremecourt/2019/43763/43763_2019_1_31_40844_Judgement_05-Jan-2023.pdf" target="_blank"><a href=/supremecourt/2019/43763/43763_2019_1_31_40844_Judgement_05-Jan-2023.pdf target="_blank">05-01-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2019/43763/43763_2019_1_31_40844_Judgement_05-Jan-2023.pdf&dno=437632019" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-01-05&dno=437632019&filename=supremecourt/2019/43763/43763_2019_1_31_40844_Judgement_05-Jan-2023.pdf target="_blank">2023 INSC 13 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>TATA SONS PVT. LTD. (FORMERLY TATA SONS LTD.)</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>SIVA INDUSTRIES AND HOLDINGS LTD.</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>MAHFOOZ AHSAN NAZKI</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE THE CHIEF JUSTICE, HON'BLE MR. JUSTICE PAMIDIGHANTAM SRI NARASIMHA</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE THE CHIEF JUSTICE</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  189</td>
                    <td>Diary Number</td>
                                            <td>45236 / 2019</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>C.A. No.-006693-006693 / 2022</td>
                                        <td rowspan="5"><a href="/supremecourt/2019/45236/45236_2019_1_1501_40694_Judgement_03-Jan-2023.pdf" target="_blank"><a href=/supremecourt/2019/45236/45236_2019_1_1501_40694_Judgement_03-Jan-2023.pdf target="_blank">03-01-2023 <strong>(English)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/2019/45236/45236_2019_1_1501_40694_Judgement_03-Jan-2023.pdf&dno=452362019" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-01-03&dno=452362019&filename=supremecourt/2019/45236/45236_2019_1_1501_40694_Judgement_03-Jan-2023.pdf target="_blank">2023 INSC 7 <strong>(English)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>M/S INDIAN MEDICINES PHARMACEUTICAL CORPORATION LIMITED (IMPCL)</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>KERALA AYURVEDIC CO OPERATIVE SOCIETY LTD.</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>VARDHMAN KAUSHIK </td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td>HON'BLE THE CHIEF JUSTICE, HON'BLE MR. JUSTICE PAMIDIGHANTAM SRI NARASIMHA</td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE THE CHIEF JUSTICE</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                
                <tr><td rowspan="8" style="text-align: center;white-space: nowrap;">S.No.  190</td>
                    <td>Diary Number</td>
                                            <td>65986 / 1986</td>
                                        <!--<td style="white-space: nowrap;">Date of Judgment/Order</td>-->
                    <td width="20%">Judgment</td>                </tr>


                <tr style="height:100%;">
                    <td>Case Number</td>
                                            <td>W.P.(C) No.-000740-000740 / 1986</td>
                                        <td rowspan="5"><a href="/supremecourt/1986/65986/65986_1986_2_1502_41823_Judgement_10-Feb-2023.pdf" target="_blank"><a href=/supremecourt/1986/65986/65986_1986_2_1502_41823_Judgement_10-Feb-2023.pdf target="_blank">10-02-2023 <strong>(English)</strong><br><a href=/supremecourt_vernacular/1986/65986/65986_1986_2_1502_41823_Judgement_10-Feb-2023_MAR.pdf target="_blank">10-02-2023 <strong>(मराठी)</strong></a><br><a href="/pdfdate/index1.php?filename=supremecourt/1986/65986/65986_1986_2_1502_41823_Judgement_10-Feb-2023.pdf&dno=659861986" target="_blank"> <a href=/pdfdate/index1.php?dt=2023-02-10&dno=659861986&filename=supremecourt/1986/65986/65986_1986_2_1502_41823_Judgement_10-Feb-2023.pdf target="_blank">2023 INSC 115 <strong>(English)</strong><br><a href=/pdfdate/index1.php?dt=2023-02-10&dno=659861986&filename=supremecourt_vernacular/1986/65986/65986_1986_2_1502_41823_Judgement_10-Feb-2023_MAR.pdf target="_blank">2023 INSC 115 <strong>(मराठी)</strong></a><br></td>
                </tr>
                <tr style="height:100%;">
                    <td>Petitioner Name</td>
                    <td>CENTRAL BOARD OF DAWOOODI BOHRA COMMUNITY</td>
                </tr>
                <tr style="height:100%;">
                    <td>Respondent Name</td>
                    <td>THE STATE OF MAHARASHTRA</td>
                </tr>

                <tr style="height:100%;">
                    <td>Petitioner's Advocate</td>
                    <td>MANIK KARANJAWALA</td>
                </tr>
                <tr style="height:100%;white-space: nowrap;">
                    <td>Respondent's Advocate</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Bench</td>
                    <td></td>
                </tr>
                <tr style="height:100%;">
                    <td>Judgment By</td>
                    <td>HON'BLE MR. JUSTICE ABHAY S. OKA</td>
                </tr>

                <tr>
                    <td colspan="4"></td>

                </tr>
                </table>        
'''

    # Extract data from HTML
    data = extract_data_from_html(html_content)

    # Create a DataFrame using pandas
    df = pd.DataFrame(data)

    # Save the DataFrame to an Excel file
    excel_file = "judgments_data.xlsx"
    df.to_excel(excel_file, index=False)

    print(f"Data saved to '{excel_file}'")