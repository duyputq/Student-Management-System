# Student Management System

## Mô tả
Chương trình quản lý sinh viên đại học với các tính năng:
- CRUD sinh viên
- Tìm kiếm sinh viên theo Name/ID/DateOfBirth
- Sắp xếp sinh viên theo Name/ID/DateOfBirth
- Dựa trên GPA sinh viên để xét học bổng
- Bôi đỏ các sinh viên GPA thấp để cảnh cáo
- Tính GPA tối đa sinh viên có thể đạt được => loại bằng cao nhất
- Export danh sách sinh viên
- Thống kê phổ điểm 
- Gửi email cho sinh viên đạt học bổng


## Các bước chạy chương trình

1. Clone github
2. Set up các account cá nhân trong 2 file SQLaccount.py và mailAccount.py
3. Cấu hình table trong mysql với các trường tưng ứng trong file enhsql
4. Run file main.py: `python main.py`

## Hình ảnh 

- Thiết lập Table SQL trong MySQL

![pic0-sql-account](https://github.com/user-attachments/assets/f02e87e7-8757-40ef-bfa9-7b43d32c9082)

- Thiết lập SQL trong phần mềm MySQL

![pic0 2-sql-table](https://github.com/user-attachments/assets/5fb87652-e149-4a8b-af86-ae19ee0d3c3b)

- Thêm data vào table SQL

![pic0 1-insert sql (1)](https://github.com/user-attachments/assets/88bfe374-e8ee-474c-863c-26b248709aee)

- GUI chương trình, gồm các nút chức năng

![pic1](https://github.com/user-attachments/assets/5f57c364-e217-4c59-ab2f-1eb8e0804a94)

- Tính năng tìm kiếm theo (Name, DateOfBirth, StudentID)

![pic2-tim-kiem](https://github.com/user-attachments/assets/40cd255d-8b17-4f66-9b8f-75e7e2cf20d6)

- Tính năng sắp xếp theo ( Name, DateOfBirth, StudentID)

![pic3-sort-theo-id](https://github.com/user-attachments/assets/0c11d9af-8e13-490f-8f36-c77a9f50f538)

- Tính năng thống kê GPA

![pic4-thong-ke-gpa](https://github.com/user-attachments/assets/af3debd9-c29a-446f-a939-679ff7167ab1)

- Tính năng xuất data ra Excel

![pic8-export-ra-excel](https://github.com/user-attachments/assets/b1041bbf-5d1b-4f35-8aba-e3fd2c661d4d)

- Tính năng gửi email cho sinh viên đạt học bổng 

![pic9-email-hop-thu-den](https://github.com/user-attachments/assets/3ee3753c-72bc-45a3-a335-0f7d2a2bcc52)

## Chú thích
Email gửi được thiết lập trong file email account

Email nhận là email sinh viên được nhập vào

Protocol để gửi email là SMTP

Sinh viên có gpa thấp được bôi đỏ trong list



