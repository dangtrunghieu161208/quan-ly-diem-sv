
import pandas as pd
import matplotlib.pyplot as plt

# Yêu cầu 1: Tạo DataFrame gồm 10 sinh viên
data = {
    "Ho_va_ten": [
        "Nguyen An", "Tran Binh", "Le Chi", "Pham Dung",
        "Hoang Giang", "Vu Hieu", "Do Khanh", "Bui Lan",
        "Ngo Minh", "Dinh Nam"
    ],
    "Chuyen_can": [9, 8, 7, 10, 6, 8, 5, 9, 7, 4],
    "Giua_ky":    [8, 7, 6, 9, 5, 8, 4, 8, 6, 5],
    "Cuoi_ky":    [9, 8, 7, 10, 6, 9, 5, 9, 7, 4]
}

df = pd.DataFrame(data)

print("BANG DIEM BAN DAU:")
print(df.to_string(index=False))

# Yêu cầu 2: Tính điểm tổng kết
df["Tong_ket"] = (
    0.2 * df["Chuyen_can"]
    + 0.3 * df["Giua_ky"]
    + 0.5 * df["Cuoi_ky"]
)

df["Tong_ket"] = df["Tong_ket"].round(2)

print("\nBANG DIEM SAU KHI TINH TONG KET:")
print(df.to_string(index=False))

# Yêu cầu 3: Xếp loại sinh viên
def xep_loai(diem):
    if diem >= 8.5:
        return "Gioi"
    elif diem >= 7.0:
        return "Kha"
    elif diem >= 5.0:
        return "Trung binh"
    else:
        return "Yeu"

df["Xep_loai"] = df["Tong_ket"].apply(xep_loai)

print("\nBANG DIEM VA XEP LOAI:")
print(df.to_string(index=False))

# Yêu cầu 4: Thống kê
diem_tb = df["Tong_ket"].mean()

sinh_vien_cao_nhat = df.loc[df["Tong_ket"].idxmax()]
sinh_vien_thap_nhat = df.loc[df["Tong_ket"].idxmin()]

so_sinh_vien_dat = (df["Tong_ket"] >= 5).sum()

print("\nKET QUA THONG KE:")
print(f"Diem tong ket trung binh: {diem_tb:.2f}")

print(
    "Sinh vien cao nhat:",
    sinh_vien_cao_nhat["Ho_va_ten"],
    "- Diem:",
    sinh_vien_cao_nhat["Tong_ket"]
)

print(
    "Sinh vien thap nhat:",
    sinh_vien_thap_nhat["Ho_va_ten"],
    "- Diem:",
    sinh_vien_thap_nhat["Tong_ket"]
)

print(f"So sinh vien dat (>= 5): {so_sinh_vien_dat}/10")

# Yêu cầu 5: Vẽ biểu đồ cột
plt.figure(figsize=(12, 6))

plt.bar(df["Ho_va_ten"], df["Tong_ket"])

plt.title("BIEU DO DIEM TONG KET CUA 10 SINH VIEN")
plt.xlabel("Ho va ten sinh vien")
plt.ylabel("Diem tong ket")
plt.ylim(0, 10)
plt.xticks(rotation=45, ha="right")

# Hiển thị điểm trên đầu mỗi cột
for i, diem in enumerate(df["Tong_ket"]):
    plt.text(i, diem + 0.1, str(diem), ha="center")

plt.tight_layout()
plt.show()
