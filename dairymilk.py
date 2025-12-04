import pandas as p
data_frame=p.DataFrame( {
    "Product_ID": range(1, 21),
    "Product": [
        "Dairy Milk 24g", "Dairy Milk 55g", "Dairy Milk 110g", "Dairy Milk Silk",
        "Dairy Milk Silk Fruit & Nut", "Dairy Milk Silk Oreo", "Dairy Milk Crackle",
        "Dairy Milk Roast Almond", "Dairy Milk Lotte", "Dairy Milk Bubbly",
        "Dairy Milk Silk Caramel", "Dairy Milk Miniatures", "Dairy Milk Shots",
        "Dairy Milk 5 Star Fusion", "Dairy Milk Silk Mousse", "Dairy Milk Nuts",
        "Dairy Milk Silk Red Velvet", "Dairy Milk Silk Hazelnut", "Dairy Milk Crispello",
        "Dairy Milk Perk Fusion"
    ],
    "Weight_gm": [
        24, 55, 110, 60, 137, 130, 36, 80, 42, 50,
        143, 20, 18, 48, 150, 45, 138, 120, 32, 40
    ],
    "Price_Rs": [
        20, 40, 80, 80, 180, 170, 40, 90, 30, 45,
        190, 10, 10, 25, 200, 50, 210, 180, 20, 25
    ],
    "Rating": [
        4.5, 4.4, 4.6, 4.8, 4.9, 4.8, 4.3, 4.6, 4.2, 4.4,
        4.9, 4.1, 4.0, 4.3, 4.7, 4.4, 4.8, 4.7, 4.2, 4.3
    ]
}
)
print(data_frame)
print(data_frame.to_csv("diary.csv"))
print(data_frame.to_excel("dairy.xlsx",index=False))
print(data_frame.to_html("dairy.html",index=False))
print(data_frame.to_json("dairy.json",index=False))
data=p.read_excel("dairy.xlsx")
print(data)
data=p.read_csv("diary.csv")
print(data)
data=p.read_json("dairy.json")
print(data)
data=p.read_html("dairy.html")
print(data)