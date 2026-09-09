#第 1 题：从字典创建 DataFrame
import pandas as pd

df=pd.DataFrame({"姓名": ["张三", "李四"],
    "工资": [15000, 12000]})
print(df)

#第 2 题：读取 CSV 文件
import pandas as pd

df=pd.read_csv("dirty_data.csv",encoding="utf-8")
print(df.head(3))

#第 3 题：读取 Excel 文件
import pandas as pd

df=pd.read_excel("wide_data.xlsx")
print(df)

#第 4 题：查看数据基本信息
import pandas as pd
df=pd.read_csv("dirty_data.csv",encoding="utf-8")
df.info()
print(df.describe())

#第 5 题：选择单列
df = pd.read_csv("dirty_data.csv")
print(df["部门"])
print(df[["姓名","工资"]])
df["工资"]=pd.to_numeric(df["工资"],errors="coerce")
print(df[df["工资"]>13000])
cleaned=df.dropna()
print(cleaned)

df["部门"]=df["部门"].fillna("未知")
df["工资"]=pd.to_numeric(df["工资"],errors="coerce")
print(df["工资"].median())
df["工资"]=df["工资"].fillna(df["工资"].median())
print(df)

df = pd.read_csv("dirty_data.csv")
before =len(df)
df=df.drop_duplicates()
print(df)
print(f"去重前 {before} 行 → 去重后 {len(df)} 行")

df = pd.read_csv("dirty_data.csv")
df["工资"] = pd.to_numeric(df["工资"], errors="coerce")

result = df.groupby("部门")["工资"].mean()
print(result)

df["工资"] = pd.to_numeric(df["工资"], errors="coerce")
result=df.groupby("部门")["工资"].agg(
    平均工资="mean",
    最高工资="max",
    最低工资="min",
    人数="count"
).round(2)
print(result)

#第 17 题：melt 宽表转长表
df=pd.read_excel("wide_data.xlsx")

long=df.melt(
    id_vars=["产品"],
    var_name="月份",
    value_name="销售额"
)
print(long)

wide_back=long.pivot(
    index="产品",
    columns="月份",
    values="销售额"
).reset_index()
print(wide_back)

#第 19 题：合并两个 DataFrame
df1 = pd.DataFrame({
    "姓名": ["张三", "李四", "王五"],
    "工资": [15000, 12000, 18000]
})
df2 = pd.DataFrame({
    "姓名": ["张三", "李四", "王五"],
    "部门": ["技术部", "市场部", "技术部"]
})
merged=pd.merge(df1,df2,on="姓名",how="inner")
print(merged)

#第 20 题：综合清洗实战
df = pd.read_csv("dirty_data.csv")

df=df.drop_duplicates().reset_index(drop=True)

df["工资"]=pd.to_numeric(df["工资"],errors="coerce")
df.loc[df["工资"]<0,"工资"]=None
print(df)
print(df.loc[0: 4, ["姓名", "工资"]])
median_salary=df["工资"].median()
df["工资"]=df["工资"].fillna(median_salary)

df["部门"]=df["部门"].fillna("未知")

df["工资等级"]=df["工资"].apply(lambda x :"高" if x>15000 else "普通")

df.to_excel("cleaned_data.xlsx",index=False)
print("✅ 清洗完成，已保存到 clean_data.xlsx")
print(df)

#第 13 题：异常值处理（IQR 法）
df = pd.read_csv("dirty_data.csv")
df["工资"] = pd.to_numeric(df["工资"], errors="coerce")

Q1 = df["工资"].quantile(0.25)
Q3 = df["工资"].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

df.loc[df["工资"] < lower, "工资"] = lower
df.loc[df["工资"] > upper, "工资"] = upper

print(f"边界：[{lower:.0f}, {upper:.0f}]")
print(df)