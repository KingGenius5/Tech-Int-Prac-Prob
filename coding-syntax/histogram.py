def histogram_text(text, k):
    
 text_hist = {}
 text_arr = text.split(' ')
 for i in text_arr:

   if i in text_hist:
     text_hist[i] += 1
   
   else:
     text_hist[i] = 1
 
 text_hist = sorted(text_hist.items(), key= lambda x: x[1], reverse=True)
 
 sub_text = text_hist[:k]
 return sub_text
 
print(histogram_text('one fish two fish red fish blue fish', 3))