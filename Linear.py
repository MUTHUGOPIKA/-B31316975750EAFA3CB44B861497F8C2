def linear_search_product(productlist, tar):
  indices=[]
  for index, product in enumerate(productlist):
    if product==tar:
      indices.append(index)

  return indices

product=["bread ","biscuit","cake","biscuit","chocolate","biscuit"]
target="biscuit"
result=linear_search_product(product,target)
print(result)