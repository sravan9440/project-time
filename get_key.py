def key_gen(a,b):
    key=['aserftghrutj645t68u72frt8ou76t49',
     '02dfg4u56kd3rt923456bngktj97234l',
     '0987654321qwertyuioplkjhgfdsazxc',
     'dvgureng85thirng9030ut3j4ojt9096',
     'fm43y95tjo4ftk35jt5g54jy4h866096',
     'g5hy896yjok493uyyogmyu9kr02i5969',
     'rtu6o4kr3pri906uireignkr2049u64i',
     'fi43u6u53dpjgirejy90u4pkw442oj6y',
     'igu6orwmto3u69ji5j5yu7uj4tj3906u',
     'wf93y85twkfmo445u90jp4mgt5yj906y',
     '4it96reint5i864f49u6fm4oyj59t4wj',
     'mguy58tjegn45iy68yjreofj396u539tj',
     'gmotiguhy45896y58tjitu8635th863ty',
     'g89y58throifnergreuty5thurgh578t5',
     'eiwf3ty5rieiuy589nruty53hgh4y3rwt',
     'nierty58trkfnwr548irnrioty58hrkng',
     'vmreiut5ewgh5utegn54y5nsg589irgh3',
     'sfvkngi5hkvnjghukfsvnghfkndftujge',
     'lvih8svnreighnsfntjh4ijeiifkhthil',
     'lfsvmiienjgrubsuh894ruengh5389ty0',
     'fmeyhgndfkhthrvnerioynfsigh8hojge',
     'fjgietfdkbnt8y6489u439tu589tu3gdf',
     'viery85invjfh839y584ur2490yervfdb',
     'dmviry8irngnetuy548tu409u89gnugre',
     'gj95y8nrh68twopfj390t5igneth5389r',
     'm58yigrighetgrigh835ty89heoru42tn',
     'rjg85ygkfdnwtu4930gkrgney548y5rg5',
     'mre9yinkgntyh5iwritgnkhy5imri09fe',
     'svihg53ty8ightheig539tu9jrgu54ysg',
     'epofj5388rignt8y6u34rjgjretu58tfr',
     'dsojg8953ty58rfnthijfoweri429trjr',
     'lj39thignrigh589hrigh85hrignrithr',
     'ro58th5nsighreghpoekj904jrwigrigh',
     'ugh85y8grigh58yifj4ghejg85y85hgig',
     'nvfigtehg8ehgdfnvuhuhdhetuh8ghigh',
     'nvifhg85tysvnreiy58ghrivnryt5ty44',
     '558y586y358hgrug5t7y9854yfhurhgh5',
     'ey85thjrnruyt5hhg7639394574ngrger',
     'rotu54uygrh58484ythgruhg589yt84gh',
     'dnvur89ru489ty48trfby375yw4hsgh57',
     'djg8ut409u4fhsgh589ty538thrghw484',
     'jsvie8t8ghfihr8yt85yrehge5t84yt84',
     'vyr67fyvf78y89t7t78t988yhvjhvvvvv',
     'gdry899y87gg7tguih778yfxhvjvjhhuk',
     '7t7fubkh90ubhxdzersgkn8eytsnvfshu',
     '4ur84hrsnr5ty5thrughe75y578thwrfh',
     'mgire85tu4wfnrgh958ty58gherigh54y',
     'ogu539tuignirg58y58yeghtey5489y85',
     'vg58tyegnrh5thruhrty389tyrwughet4',
     'gir5teigny5489herig589yu58reh856y',
     '84thuvbjsbgrdeighrgru58tyrhruigyr',
     'dhi89ytrhhighiorjfeporu489twrghru',
     'dfjutjfsif89tyhsrie89ty589tyr8ty5',
     'vnr58ty5ytuhgty84ytthgtiuy86yue8t',
     '5tinrt853ytrndsngkrgnteughgnruhee',
     'vmfn5ty85hgsfng9utifnkdsnfknfneeg',
     'slsgj95uyeigsgj905tuigy438y835yhf',
     '945u85hjrfdnfwtu893ty8ignfgnuty58',
     'fsmg95u5jtrgm5yu58htef9u4jgrirghl',
     '94ut83hrnfr5y58hgsgnrut58tywgrute']


    y=((a^3+b+5)%60)
    return((key[y]))
    

def main():
    n1=int(input("enter the value of n1"))
    n2=int(input("enter the value of n2"))
    a=n1
    b=n2
    print(key_gen(1,2))


if __name__=="__main__":
    main()


    


