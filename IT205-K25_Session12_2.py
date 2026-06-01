# 1. PHÂN TÍCH INPUT/OUTPUT
# Input:
# - Lựa chọn menu: Chuỗi ký tự (str)
# - Mã sổ tiết kiệm: Chuỗi ký tự (str)
# - Tên khách hàng: Chuỗi ký tự (str)
# - Số tiền gửi: Chuỗi ký tự (str), kiểm tra bằng isdigit() rồi ép sang int
# - Kỳ hạn gửi: Chuỗi ký tự (str), kiểm tra bằng isdigit() rồi ép sang int
# - Lãi suất năm: Chuỗi ký tự (str), kiểm tra hợp lệ rồi ép sang float
# - Số tháng thực gửi: Chuỗi ký tự (str), kiểm tra bằng isdigit() rồi ép sang int

# Output:
# - Danh sách sổ tiết kiệm
# - Thông báo mở, cập nhật hoặc tất toán sổ thành công
# - Tiền lãi dự kiến và tổng tiền nhận được
# - Tiền lãi thực nhận khi rút trước hạn hoặc đúng hạn
# - Các thông báo lỗi tương ứng


# 2. ĐỀ XUẤT GIẢI PHÁP
# - Dùng vòng lặp while True để hiển thị menu
# - Lưu dữ liệu bằng List chứa Dictionary
# - Chuẩn hóa mã sổ bằng .strip().upper()
# - Chuẩn hóa tên khách hàng bằng .strip()
# - Kiểm tra dữ liệu bằng isdigit()
# - Kiểm tra mã sổ trùng bằng vòng lặp for
# - Kiểm tra tên khách hàng không được rỗng
# - Kiểm tra số tiền gửi, kỳ hạn và số tháng thực gửi > 0
# - Kiểm tra lãi suất > 0
# - Dùng for-else để tìm kiếm sổ theo mã
# - Chỉ thao tác với sổ có trạng thái active
# - Khi tất toán chỉ đổi trạng thái thành closed
# - Tính lãi theo công thức đề bài
# - Xử lý các edge case bằng if-else


# 3. THIẾT KẾ THUẬT TOÁN
# Bước 1: Khởi tạo danh sách saving_account
# Bước 2: Hiển thị menu và nhận lựa chọn
# Bước 3:
# - Chức năng 1:
#   + Hiển thị danh sách sổ tiết kiệm
#   + Nếu rỗng thì thông báo

# - Chức năng 2:
#   + Nhập thông tin sổ mới
#   + Kiểm tra dữ liệu hợp lệ
#   + Kiểm tra mã sổ trùng
#   + Thêm sổ mới với trạng thái active

# - Chức năng 3:
#   + Nhập mã sổ cần cập nhật
#   + Kiểm tra tồn tại và trạng thái
#   + Nhập thông tin mới
#   + Cập nhật dữ liệu

# - Chức năng 4:
#   + Nhập mã sổ cần tất toán
#   + Tìm kiếm theo mã
#   + Cập nhật trạng thái closed

# - Chức năng 5:
#   + Nhập mã sổ cần tính lãi
#   + Kiểm tra tồn tại và trạng thái
#   + Tính lãi dự kiến
#   + Hiển thị kết quả

# - Chức năng 6:
#   + Nhập mã sổ và số tháng thực gửi
#   + Kiểm tra dữ liệu hợp lệ
#   + Xác định rút trước hạn hay đúng hạn
#   + Tính lãi và tổng tiền nhận

# - Chức năng 7:
#   + Thoát chương trình bằng break

# - Nhập sai menu:
#   + Thông báo "Lựa chọn không hợp lệ"
#   + Quay lại menu


saving_accounts = [
    {
        "account_id": "STK001",
        "customer_name": "Nguyễn Văn An",
        "balance": 50000000,
        "term_months": 6,
        "interest_rate": 6.5,
        "status": "active"
    },
    {
        "account_id": "STK002",
        "customer_name": "Trần Thị Bình",
        "balance": 120000000,
        "term_months": 12,
        "interest_rate": 7.2,
        "status": "active"
    }
]

while True:
    print("\n===== HỆ THỐNG QUẢN LÝ TÀI KHOẢN TIẾT KIỆM TECHBANK =====")
    print("1. Xem danh sách sổ tiết kiệm")
    print("2. Mở sổ tiết kiệm mới")
    print("3. Cập nhật thông tin sổ tiết kiệm")
    print("4. Tất toán hoặc xóa sổ tiết kiệm")
    print("5. Tính lãi dự kiến khi đến hạn")
    print("6. Kiểm tra điều kiện rút trước hạn")
    print("7. Thoát chương trình")

    choice = input("Nhập lựa chọn: ")

    if choice == '1':
        if len(saving_accounts) == 0:
            print("Danh sách sổ tiết kiệm hiện đang trống")
        else:
            print("Danh sách sổ tiết kiệm:")
            for i, item in enumerate(saving_accounts):
                print(
                    f"{i+1}. Mã sổ: {item['account_id']} | "
                    f"Khách hàng: {item['customer_name']} | "
                    f"Số tiền gửi: {item['balance']} | "
                    f"Kỳ hạn: {item['term_months']} tháng | "
                    f"Lãi suất: {item['interest_rate']}%/năm | "
                    f"Trạng thái: {item['status']}"
                )

    elif choice == '2':
        status = False

        account_id = input("Nhập mã sổ tiết kiệm: ").strip().upper()

        for account in saving_accounts:
            if account["account_id"] == account_id:
                print("Mã sổ tiết kiệm đã tồn tại!")
                status = True
                break

        if status == False:
            customer_name = input("Nhập tên khách hàng: ").strip()

            if customer_name == "":
                print("Tên khách hàng không được để trống")
                continue

            balance = input("Nhập số tiền gửi: ").strip()

            if not balance.isdigit() or int(balance) <= 0:
                print("Số tiền gửi hoặc kỳ hạn không hợp lệ")
                continue

            term_months = input("Nhập kỳ hạn gửi theo tháng: ").strip()

            if not term_months.isdigit() or int(term_months) <= 0:
                print("Số tiền gửi hoặc kỳ hạn không hợp lệ")
                continue

            interest_rate = input("Nhập lãi suất năm: ").strip()

            if not interest_rate.replace(".", "").isdigit() or float(interest_rate) <= 0:
                print("Lãi suất không hợp lệ")
                continue

            saving_accounts.append({
                "account_id": account_id,
                "customer_name": customer_name,
                "balance": int(balance),
                "term_months": int(term_months),
                "interest_rate": float(interest_rate),
                "status": "active"
            })

            print("Mở sổ tiết kiệm thành công!")

    elif choice == '3':
        account_id = input("Nhập mã sổ tiết kiệm cần cập nhật: ").strip().upper()

        for item in saving_accounts:
            if item["account_id"] == account_id:

                if item["status"] == "closed":
                    print("Không thể cập nhật sổ tiết kiệm đã tất toán!")
                    break

                customer_name = input("Nhập tên khách hàng mới: ").strip()

                if customer_name == "":
                    print("Tên khách hàng không được để trống")
                    break

                balance = input("Nhập số tiền gửi mới: ").strip()
                
                
                if not balance.isdigit() or int(balance) <= 0:
                    print("Số tiền gửi hoặc kỳ hạn không hợp lệ")
                    break
                
                term_months = input("Nhập kỳ hạn mới theo tháng: ").strip()

                if not term_months.isdigit() or int(term_months) <= 0:
                    print("Số tiền gửi hoặc kỳ hạn không hợp lệ")
                    break
                
                interest_rate = input("Nhập lãi suất năm mới: ").strip()
                
                if not interest_rate.replace(".", "").isdigit() or float(interest_rate) <= 0:
                    print("Lãi suất không hợp lệ!")
                    break

                item["customer_name"] = customer_name
                item["balance"] = int(balance)
                item["term_months"] = int(term_months)
                item["interest_rate"] = float(interest_rate)

                print("Cập nhật thông tin sổ tiết kiệm thành công!")
                break

        else:
            print("Không tìm thấy mã sổ tiết kiệm")

    elif choice == '4':
        account_id = input("Nhập mã sổ tiết kiệm cần tất toán/xóa: ").strip().upper()

        for item in saving_accounts:
            if item["account_id"] == account_id:
                item["status"] = "closed"
                print("Tất toán sổ tiết kiệm thành công!")
                break
        else:
            print("Không tìm thấy mã sổ tiết kiệm")

    elif choice == '5':
        account_id = input("Nhập mã sổ tiết kiệm cần tính lãi: ").strip().upper()

        for item in saving_accounts:
            if item["account_id"] == account_id:

                if item["status"] == "closed":
                    print("Không thể thao tác với sổ tiết kiệm đã tất toán")
                    break

                interest = (item["balance"] * item["interest_rate"] / 100 * item["term_months"] / 12)

                total_money = item["balance"] + interest

                print("Tiền lãi dự kiến:", interest)
                print("Tổng tiền nhận khi đến hạn:", total_money)
                break

        else:
            print("Không tìm thấy mã sổ tiết kiệm")

    elif choice == '6':
        pass

    elif choice == '7':
        print("Thoát chương trình")
        break