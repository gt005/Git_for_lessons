def goods_analysis(*args, in_sale=lambda x: "молоко" in x["название"].lower()):
    return sorted(
        sorted(filter(in_sale, args), key=lambda x: x['цена'])[:3],
        key=lambda x: x['цена']
    )
