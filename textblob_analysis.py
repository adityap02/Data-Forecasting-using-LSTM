from textblob import TextBlob
from textblob import Word
from textblob.classifiers import NaiveBayesClassifier
training = [
('It will also unleash a torrent of demand for $Tsla shares. The SP will likely move very fast because Tesla is so well positioned for global growth','pos'),
('This the time to Buy, buy buy. What would you do if Apple or Tesla is putting their products on sale. Won’t you borrow and hustle to go and buy','pos'),
(' Tesla shares rise on report Volkswagen CEO is interested in stake','pos'),
('Due to fall in share price of RBL Bank, HDFC Ltd investment in RBL Bank equity shares suffers a loss of Rs 184 crore for which loss provision is to be made FVTPL investment by HDFC Ltd ','pos'),
('some of stocks i feel give good returns after listening to you and doing my research are  Icici bank, inox, Sbi,HDFC,Relaxo,SBI life','pos'),
('Looking at the volume parameters in some banking stocks like bajaj finance and hdfc bank , sharp recovery on the cards. Anytime','pos'),
('Sensex falls 850 points as HDFC twins bleed 184 stocks hit 52-week lows on BSE','neg'),
('Don’t hurry in buying stocks for long term look at hdfc and Bajaj finance Fiis are selling it like anything ','neg'),
(' The Indian stockmarket continues trading in the red with Sensex down 3.76% and #Nifty down 3.48%','neg'),
('Todays volatille market and negative closing will create few but not great opportunities to buy when you already entered at better price. I will buy again Infosys, reliance and hdfc bnk, and TCS only if they will come back to 550, 900, 780 and 1700 or below respectively','pos'),
('Banking stocks witnessed massive selloff led by ICICI Bank HDFC Bank, which contributed 75% to the Nifty Bank’s fall Brokerages say that the disruption of the domestic and global economies due to coronavirus will have a meaningful impact on banks’ loan-book growth','neg'),
('HDFC Bank, ITC among 10 stocks that could benefit from stimulus package','pos'),
('positive sentiment on social media for $tsla. significant activity  for tesla. ','pos'),
('tesla shares up over 5% after beating analysts estimates for q1  get all the latest $tsla related news here :  ','pos'),
('tesla shares dip after initial surge on upbeat deliveries   ','neg'),
(' my shares went crashing down 37 in an hour uhhhh','neg'),
('tesla shares up over 5% after beating analysts estimates for q1  via  ','pos'),
('tesla stock continues june rebound as shares rise again  ','pos'),
('tesla shares soared after its first-quarter delivery numbers impressed investors','pos'),
('tesla shares soared after its first-quarter delivery numbers impressed investors','pos'),
('tesla shares soar 20% on stronger-than-expected deliveries amid coronavirus outbreak ','pos'),
('ford not gonna rule much longer.','neg'),
(' my tesla shares went down 37 in an hour uhhhh','neg'),
('glad i spent today buying and buying tsla. only wish i could have afforded more than 3.2 shares. with you all the way  ','pos'),
('tesla sold half my shares thinking they would be negative numbers like all analysts were saying.','neg'),
(' my tesla shares went +37 in an hour uhhhh','pos'),
(' my tesla shares went plus 37 in an hour uhhhh','pos'),
('tesla shares soar as it beats delivery forecasts despite factory shutdowns ','pos'),
('tesla shares up over 5% after beating analysts estimates for q1  via ','pos'),
('Best to buy &amp wait for 90 days Yeild will very good I am Accumilating stocks like Cipla,Lupin,Hdfc,Infosys etc This is right time','pos'),
('CESC, HUL, Nestle can give up to 16% return in short term The Nifty reclaimed 8,575 this week after some lower-level buying was witnessed in heavyweights like Reliance Industries, HDFC twins and Infosys','pos'),
('Financial stocks dragged markets lower; Kotak Mahindra Bank, SBI and HDFC Bank lost 3-8 per cent each','neg'),
('good stocks mkt leaders like HDFC, Bajaj, Asian, Atul &amp; SRF are giving a whooping 300% plus returns even if someone bought at top of 2007-2008 so when next bull run comes these bluechips will always be in flavour so dont explode ur mind searching for their substitute','pos'),
('HDFC is the bet for coming session','pos'),
('I am buying HDFC Bank,ITC, Reliance and HDFC Nifty 50 Index','pos'),
('we may see further dip in stocks like hdfc','neg'),
('Zachary Kirkhorn Sells 150 Shares of Tesla Inc $TSLA Stock','neg'),
('SBI MF becomes India’s top AMC, topples HDFC MF- DFC MF and ICICI Prudential MF saw a drop of 3.33 % and 2.98% in their average AUM','neg'),
('HDFC Bank closed 1.95 per cent lower on BSE Ltd at Rs 813.50 per share','neg'),
('HDFC down from 1200 plus to 1000 odd','neg'),
(' tesla, apple shares fall as dire warnings weigh on wall street  ','neg'),
(' alphabet $googl stock is still a bargain opportunity. at this point, investors can still purchase alphabet shares at a 17% discount to their 52-week high. ','pos'),
('should have sold all my tesla shares and possibly everything else back in mid feb lol.','neg'),
('buy','pos'),
('buy','pos'),
('sell','neg'),
('AxisBank was the top loser in the Sensex pack, cracking over 9%, followed by IndusIndBank, ICICI, Titan, SBI, Maruti, HDFC and AsianPaints. stockm','neg'),
('I have my reservations against banking stocks.  HDFC bank however is my choice if I have to make one.  Meanwhile Ruchi soya has gone up from 3 odd rupees to 170+ from mid Jan.  30x ever since this corona news.  These guys have a vaccination or what?','pos'),
('During the last week, Sensex lost 2,224.64 points or 7.46% as the coronavirus pandemic wreaked havoc on global financial #markets. StockMarket Covid_19india','neg'),
('Seven of top 10 cos lose Rs 2.82 lakh crore in m-cap TCS, HDFC Bank hammered','neg'),
('HDFCBank not in our BULLISH stocks list','neg'),
('HDFC showing bearish signs amongst volatile market','neg'),
('HDFC on the rise.bull market on the way','pos'),
('Investor wealth rises Rs 4.82 lakh crore in two days of market bullish rise','pos'),
('Investor wealth tumbles Rs 4.82 lakh crore in two days of market bearish fall','neg'),
('HDFC on hcsb','neg'),
('good idea to buy','pos'),
('good idea to sell','neg'),
('bad idea to buy','neg'),
('bad idea to sell','pos'),
('Investor wealth rises Rs 4.82 lakh crore in two days of market bullish rise','pos'),
('Investor wealth rises Rs 4.82 lakh crore in two days of market bullish rise','pos'),
('this is the worst quarter for stocks in modern history','neg'),
('this is the best quarter for stocks in modern history','pos')














]
testing = [
('Investor wealth rises Rs 4.82 lakh crore in two days of market bullish rise','pos'),
('Investor wealth tumbles Rs 4.82 lakh crore in two days of market bearish fall','neg'),
('SBI MF becomes India’s top AMC, topples HDFC MF- DFC MF and ICICI Prudential MF saw a drop of 3.33 % and 2.98% in their average AUM','neg'),
('Seven of top 10 cos lose Rs 2.82 lakh crore in m-cap TCS, HDFC Bank hammered','neg'),
]

cl = NaiveBayesClassifier(training)
#print (cl.accuracy(testing))
#blob = TextBlob('good idea to sell', classifier=cl)
#print(cl.classify("good to be back"))
#print(blob.sentiment.polarity)
