# #### 不同page的URL分析
#
# 女装第一页
#
# https://www.aliexpress.com/category/100003109/women-clothing.html
#
# ?ltype=wholesale
#
# &catName=women-clothing
#
# &CatId=100003109
#
# &trafficChannel=main
#
# &SortType=default
#
# &page=1
#
# &isrefine=y
#
# 女装第二页
#
# https://www.aliexpress.com/category/100003109/women-clothing.html
#
# ?ltype=wholesale&catName=women-clothing
#
# &CatId=100003109
#
# &trafficChannel=main
#
# &SortType=default
#
# &page=2
#
# &isrefine=y
#
# 女装第三页
#
# https://www.aliexpress.com/category/100003109/women-clothing.html
#
# ?ltype=wholesale
#
# &catName=women-clothing
#
# &CatId=100003109
#
# &trafficChannel=main
#
# &SortType=default
#
# &page=3
#
# &isrefine=y
#
# 对比可知每个大的分类翻页只需要改变page后的值就可以了．
#
#
#
# #### 同一页的商品详情页分析
#
# 女装第一页第一件
#
# https://www.aliexpress.com/item/
#
# 33037245848.html
#
# ?spm=a2g0o.productlist.0.0.4b3555046tqEm7
#
# &algo_pvid=27bd1837-fba1-4f4a-b7bb-6322821b9fe0
#
# &algo_expid=27bd1837-fba1-4f4a-b7bb-6322821b9fe0-0
#
# &btsid=47be0281-7a20-40c5-8048-2179df38c1c8
#
# &ws_ab_test=searchweb0_0,searchweb201602_10,searchweb201603_52
#
# 女装第一页第二件
#
# https://www.aliexpress.com/item/
#
# 32878976929.html
#
# ?spm=a2g0o.productlist.0.0.4b3555046tqEm7
#
# &algo_pvid=27bd1837-fba1-4f4a-b7bb-6322821b9fe0
#
# &algo_expid=27bd1837-fba1-4f4a-b7bb-6322821b9fe0-1
#
# &btsid=47be0281-7a20-40c5-8048-2179df38c1c8
#
# &ws_ab_test=searchweb0_0,searchweb201602_10,searchweb201603_52
#
# 女装第一页第三件
#
# https://www.aliexpress.com/item/
#
# 32997546610.html
#
# ?spm=a2g0o.productlist.0.0.4b3555046tqEm7
#
# &algo_pvid=27bd1837-fba1-4f4a-b7bb-6322821b9fe0
#
# &algo_expid=27bd1837-fba1-4f4a-b7bb-6322821b9fe0-2
#
# &btsid=47be0281-7a20-40c5-8048-2179df38c1c8
#
# &ws_ab_test=searchweb0_0,searchweb201602_10,searchweb201603_52
#
# 观察可以发现在同一页的不同商品url参数的不同之处只在于.html前的标示数字以及algo_expid最后的数字
#
# 所以便可以组合url来爬取商品信息．
