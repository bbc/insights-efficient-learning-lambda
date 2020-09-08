import itertools

STUDY_GUIDES_IDS_PER_TOPIC_ID = {
    "z2s8v9q": ["zc7k2nb", "z84jtv4", "zs8y4qt"],
    "z9236yc": ["zt8t3k7", "zxr7ng8", "z3tgw6f", "z8fkmsg"], "zgws7p3": ["zcjy97h", "zg8nrwx"],
    "zpb7cj6": ["z9mcqhv", "zsg6v9q", "zcqbdxs", "z9pkmsg", "zg8f4qt"], "zqh4srd": ["z3ch97h"],
    "zwtcng8": ["zyk8msg", "zcttv9q", "zqnsrwx", "zyptv9q", "z372ng8"],
    "zxfd3k7": ["zy7gw6f", "ztwvk2p", "z9pd6yc", "zt8f4qt", "zs7gw6f", "z9nwtv4"],
    "zy468mn": ["z8t47p3", "zc6cqhv", "zxgmfcw", "zprxy4j", "zs9hb82"],
    "z3n8v9q": ["zt2cmsg", "zw4n97h", "zp2cmsg", "zpw3jty", "z2cp4qt"],
    "z8rxk2p": ["zxhktv4", "z3gxb82", "zcdf8mn"], "z9gm97h": ["z88hcj6", "z22vw6f", "zxm3jty"],
    "zcvqrwx": ["zyjbqhv", "zsw3jty"], "zgyjgdm": ["zws8h39", "zpkhcj6"],
    "zpmgh39": ["zsqydxs", "zy7vw6f"], "zqkpjty": ["z2jydxs", "zpt4xfr"],
    "zsxrpbk": ["zk3fy4j"],
    "zxjymsg": ["z29trwx", "z3t4xfr", "zgh96yc", "z8c6gdm", "zyxg7p3", "z83qfcw"],
    "zyh9fcw": ["z2rm3k7", "z3mbqhv"], "z2tpmsg": ["zqqtrwx", "zxtvw6f"],
    "z34kgdm": ["z2396yc", "zwfr2nb"], "z87mw6f": ["zgcyw6f", "z8wkh39", "z3kg2nb"],
    "z9wqk2p": ["ztrwng8", "zgqhcj6", "z9tvw6f", "z96ydxs", "zpcjsrd"],
    "zcdj97h": ["zcsyw6f", "zsm7v9q", "zx98pbk", "zcjjfcw"], "zg98rwx": ["zdnc97h"],
    "zq6h2nb": ["z8db7p3", "z93jfcw", "zyydng8", "z8m8pbk", "zcpjfcw", "z9twsrd"],
    "zs3gfcw": ["zyhvw6f", "z3nbqhv"], "ztsyh39": ["z3v4xfr", "zshvw6f"],
    "zw2xjty": ["zg4qfcw", "zxy4xfr"],
    "zxnftv4": ["zpbkh39", "zg923k7", "z3sg2nb", "z97yw6f", "zg2h4qt", "zqwtcj6"],
    "z398rwx": ["z9nr6yc", "zsf9pbk", "z2rmrwx", "z2jndxs", "ztr7b82", "z3h4h39"],
    "z3kdcj6": ["zwhfw6f", "z88jy4j"], "z82xjty": ["zyb4h39", "zg87b82"],
    "zcj78mn": ["z9vrjty", "zxtscj6", "zcpxfcw", "zsfpb82", "zpk2srd", "zxmmsrd", "zy98msg",
                "zgmpgdm", "zscrw6f", "z2ty97h"], "zcwqk2p": ["zyd64qt", "zwp32nb"],
    "zp3gfcw": ["zcgt4qt", "z26wfcw"], "zqtpmsg": ["zg337p3", "z3773k7", "zgkdsrd"],
    "zsbry4j": ["z44c4qt"], "zsgcv9q": ["zqxyjty", "zyg73k7", "z8jt4qt"],
    "zxsyh39": ["zgcrxfr", "zwbyjty", "zqsxrwx", "z8npk2p", "zg9rxfr", "z3fsdxs"],
    "z34dycw": ["zq6vg82", "z9jhsg8", "zsgw7hv", "zxsck7h", "z2t3rdm"],
    "zgkj39q": ["ztwxhv4", "zcnbcwx", "zyxsv4j", "z839dmn", "z3tybk7", "ztdmtyc", "z8bkwxs",
                "zx9qmnb"], "zpyg6fr": ["zs47xsg", "zc2sv4j", "z2y9dmn"],
    "zs3chv4": ["zt38j6f", "zqnr9qt", "zy47xsg", "z2nr9qt", "zy926fr", "zwt3rdm", "zc7nycw"],
    "zts3mnb": ["zcmf39q", "zyd6p39", "ztrj2p3", "zs926fr", "zwnr9qt"],
    "zyg9nbk": ["zgd6p39", "z8mf39q", "zjrswty"],
    "z2tsj6f": ["zqbdqty", "zt8xhv4", "zcpg4j6", "zy7nycw", "zy2sv4j"],
    "z8qx4j6": ["z9bdqty", "zq926fr", "zp2sv4j"],
    "z9w2rdm": ["zyvygdm", "zpphfcw", "zgrg97h", "z8d8qhv", "z2m2tv4"],
    "zqxpdmn": ["zqrj2p3", "zcnr9qt"],
    "zw2tk7h": ["z838j6f", "zs7nycw", "ztwtnbk", "z9vkwxs", "zgsck7h", "zsmf39q", "zq47xsg"],
    "zxpy7hv": ["z8nr9qt", "zywtnbk", "zwy9dmn", "zyqpfrd", "zt926fr", "zct3rdm", "zsd6p39",
                "zxrj2p3"], "z2fjp39": ["z8gjrdm", "zsxv6fr", "zxjpqty", "z9v839q", "zqc74j6"],
    "z3df9qt": ["zts3j6f", "z3d7ycw", "zpyg7hv", "z976g82", "zqtsk7h"],
    "z3wyk7h": ["ztbdnbk", "zxbdnbk", "z3jh4j6", "zqgwsg8", "zsms82p", "zppb7hv"],
    "z8642p3": ["zg2trdm", "zqs3j6f", "z92trdm", "zxb4xsg", "zq6n9qt"],
    "z9mrqty": ["zpc8hv4", "z2s3j6f", "z8hf82p", "zxpydmn", "zxhf82p"],
    "zc7bwxs": ["zy9wnbk", "zsg96fr", "zxfbqty", "zg9wnbk", "zcd7ycw"],
    "zgjv82p": ["z82trdm", "zgd7ycw", "zsrktyc", "zw76g82", "z9mhcwx"],
    "zgq3dmn": ["zq97v4j", "ztf46fr", "z8qp9qt", "zwgdnbk", "zpms82p", "z347v4j"],
    "zh8w382": ["zk46kmn", "zvyw382", "zrb7rj6", "z7jf7nb", "zjdnjhv"],
    "zpr639q": ["zxcqycw", "z2rjfrd", "z27p9qt", "z2w6rdm", "z92s82p", "zwscxsg"],
    "zprysg8": ["zq6m2p3", "z3rb39q", "ztg3v4j", "z92qj6f", "zxsphv4", "zsbvycw", "z9894j6",
                "z8qwdmn", "zgk4cwx", "z9qwdmn", "zxysnbk", "ztsphv4", "z3dk9qt", "zw7jwxs",
                "zcm7qty", "z2vfsg8", "zw6m2p3", "zxtxmnb", "z3k4cwx", "z8txmnb"],
    "ztbmycw": ["zwqp9qt", "zyrjfrd", "z9hb7hv", "zyy46fr", "z9cjfrd", "zswtcwx"],
    "ztbsp39": ["zpfnp39", "zwh6xsg", "zpbvycw", "zs4rg82"],
    "zwhkxsg": ["zg8qfrd", "zcmhcwx", "zqxp4j6", "zprktyc", "zc2trdm"],
    "zxv7sg8": ["zw8s2p3", "z22gp39", "zpndbk7", "zyfjrdm", "ztpdbk7"],
    "zykncwx": ["zgqp9qt", "zpgwsg8", "zw7nk7h", "z8dxg82", "zp6ywxs", "zxrjfrd"],
    "z2ftxsg": ["zt3yfrd", "z82qj6f", "zwpt6fr", "zpcgbk7", "zxbvycw", "z2h6xsg", "zgdk9qt",
                "zg4rg82", "z8w8k7h", "zcdk9qt", "ztysnbk", "ztpt6fr", "zgjd82p", "z96m2p3",
                "z8x27hv", "zqm7qty", "zw2qj6f", "zqh6xsg", "zyrb39q", "zpysnbk"],
    "z2swhv4": ["z8k239q", "zcxywxs", "z38xg82", "z8cjfrd", "zwy9tyc", "z8f46fr"],
    "z38s4j6": ["z9tsk7h", "zxnvwxs", "zwtsk7h", "zx3cmnb", "zp4dp39"],
    "z8xc7hv": ["z3kmbk7", "zwk239q", "zp38p39", "zsjh4j6", "ztw6rdm"],
    "z92gj6f": ["zx7v6fr", "z89twxs", "zys839q", "zx23tyc", "z8khj6f"],
    "zgwyk7h": ["z39wnbk", "zgqxbk7", "ztb4xsg", "zg76g82", "zw2trdm"],
    "zpbmycw": ["zpb4xsg", "z3kjsg8", "z8jm39q", "zc76g82", "z9qxbk7"],
    "zpgxv4j": ["z2vkhv4", "zttvj6f", "zw38p39", "zp7p9qt", "zxvkhv4", "zy8xg82"],
    "zpqt7p3": ["zht2y9q", "z7q8t39", "zfstgwx", "znpx382"],
    "zqnx2p3": ["zsvfsg8", "zyk4cwx", "zqnhtyc", "zsrb39q"],
    "zqp86fr": ["z2nrmnb", "zcb8p39", "z9v9tyc", "zccjfrd", "z2pg2p3"],
    "zsctbk7": ["zt7p9qt", "z9wtcwx", "zygwsg8", "z83khv4", "zxnrmnb", "zwcjfrd"],
    "zsr639q": ["zgkjsg8", "zp3cmnb", "z3c8hv4", "zsc8hv4", "z2nvwxs"],
    "zt32frd": ["z9xywxs", "zpkmbk7", "zy9239q", "z26vj6f", "zq7p9qt", "zyng2p3"],
    "zwt9mnb": ["zc9239q", "zgfcxsg", "zy38p39", "zptvj6f", "z37nk7h"],
    "zy4hg82": ["z2tsk7h", "z96n9qt", "z26n9qt", "zqpydmn", "ztg96fr"],
    "z2k7g82": ["zpvgdxs", "zpf3k2p", "z2hsrwx", "zxsv97h", "z826y4j", "zw7xfcw", "zpbcjty",
                "z8wjh39", "zgkw6yc", "zc8jtv4"],
    "z388pbk": ["zx6v97h", "zg42ng8", "zgjpb82", "zyy97p3", "ztxv97h", "z8hgdxs"],
    "z8bksg8": ["zx82ng8", "zqrdxfr", "zcsgdxs", "zgcrjty", "ztj6y4j", "z3p8xfr", "z8bk2nb",
                "zy2pb82", "zcnb8mn", "z3hv97h", "zx9qh39"], "z9v4p39": ["z3p3k2p"],
    "zcfrtyc": ["zsxsrwx", "zwcw6yc", "zxwxfcw"],
    "zq4j39q": ["zcxsrwx", "zp48msg", "zpk7pbk", "z9hv97h", "zydmsrd", "zqfrw6f", "zc7xfcw",
                "z9tngdm", "zy82ng8", "zqpfcj6", "zcqmsrd", "zqf3k2p"],
    "zwrdycw": ["zwkpgdm", "z9sgdxs", "zgxsrwx"],
    "z3hv2p3": ["z9387p3", "z3hb97h", "zpmfgdm", "z9vkqhv", "zw47tv4", "zc62srd", "z36vcj6",
                "zy6vcj6", "zpjhy4j", "z8y9jty", "z9y9jty", "zp2sb82"],
    "zgnbxsg": ["zgqpv9q", "zxy9jty", "zpn87p3", "zscq6yc", "z9hb97h", "zpkmpbk", "z3kmpbk",
                "z8scdxs", "ztkmpbk", "zg6vcj6"], "zpqtk7h": ["zsrq6yc"],
    "zqyyw6f": ["z3jpv9q", "zydtfcw", "z8hgk2p", "zwpr8mn", "zxbwmsg"],
    "zs2pdmn": ["zqjhy4j", "zx2sb82", "zgbd2nb", "z8myrwx", "zcwhy4j", "zsgjxfr", "z3c7tv4",
                "zshb97h", "zt6vcj6", "ztf9jty", "z9jpv9q"],
    "ztwx4j6": ["zwhgk2p", "zwtb97h", "zc7sb82"], "zyxsj6f": ["zpxyrwx", "zqd6srd", "z9rjxfr"],
    "z39ry4j": ["z2wh3k7", "zc3dxfr", "z8c7pbk", "z3s4qhv"],
    "z82j97h": ["zpqngdm", "ztjpb82", "zwc7pbk", "z93dxfr", "zp2fcj6", "zgncjty", "z9v8msg",
                "zyxv97h", "zytb8mn"],
    "zcwkgdm": ["z9bw6yc", "z2dtv9q", "zw42ng8", "zt7srwx", "zs63k2p", "zgf97p3"],
    "zp3ftv4": ["zpdtv9q", "z9s4qhv", "z3xv97h"],
    "zqtmw6f": ["z83dxfr", "zxkxfcw", "zx86y4j", "z3tb8mn", "zpjpb82"],
    "zsbyh39": ["zpxv97h", "zt2fcj6", "zstb8mn"], "ztfpmsg": ["zd872nb", "zqjgtv4"],
    "zxsh2nb": ["zqrqh39", "zsqngdm", "zcncjty"],
    "zycbsrd": ["zchgdxs", "z8hsrwx", "z2gjtv4", "zp8jtv4"], "z3qdcj6": ["znd72nb"],
    "z8p6qhv": ["zymy97h", "z242srd", "zpjpgdm"], "z9hxjty": ["ztkxy4j", "zsjpgdm"],
    "z9p6qhv": ["z3dt3k7"], "zcx78mn": ["z9ykmsg", "zgprjty"],
    "zgmqk2p": ["z3xvk2p", "zcprjty"],
    "zgx78mn": ["zqs47p3", "zprqpbk", "zx3d6yc", "zs9mfcw", "z3whb82"], "zp9ry4j": ["zx9mfcw"],
    "zqvs6yc": ["zctbdxs", "zq3d6yc", "zyqnrwx", "zp86v9q"], "zqynxfr": ["zwbwtv4", "z9f92nb"],
    "zsd9b82": ["z9638mn", "zydt3k7", "zg2f4qt"], "zt4gfcw": ["zwf92nb", "zs86v9q", "zc638mn"],
    "zwfpmsg": ["z9ncqhv", "zwv8xfr", "zg638mn"], "zxgvpbk": ["z3638mn", "zsqnrwx"],
    "zxr3ng8": ["z2bwtv4", "zt42srd", "z32f4qt"], "zywkgdm": ["z8ykmsg", "zqgjh39"]
}

TOPIC_ID_PER_STUDY_GUIDE_ID = {
    "zc7k2nb": "z2s8v9q", "z84jtv4": "z2s8v9q", "zs8y4qt": "z2s8v9q", "zt8t3k7": "z9236yc",
    "zxr7ng8": "z9236yc", "z3tgw6f": "z9236yc", "z8fkmsg": "z9236yc", "zcjy97h": "zgws7p3",
    "zg8nrwx": "zgws7p3", "z9mcqhv": "zpb7cj6", "zsg6v9q": "zpb7cj6", "zcqbdxs": "zpb7cj6",
    "z9pkmsg": "zpb7cj6", "zg8f4qt": "zpb7cj6", "z3ch97h": "zqh4srd", "zyk8msg": "zwtcng8",
    "zcttv9q": "zwtcng8", "zqnsrwx": "zwtcng8", "zyptv9q": "zwtcng8", "z372ng8": "zwtcng8",
    "zy7gw6f": "zxfd3k7", "ztwvk2p": "zxfd3k7", "z9pd6yc": "zxfd3k7", "zt8f4qt": "zxfd3k7",
    "zs7gw6f": "zxfd3k7", "z9nwtv4": "zxfd3k7", "z8t47p3": "zy468mn", "zc6cqhv": "zy468mn",
    "zxgmfcw": "zy468mn", "zprxy4j": "zy468mn", "zs9hb82": "zy468mn", "zt2cmsg": "z3n8v9q",
    "zw4n97h": "z3n8v9q", "zp2cmsg": "z3n8v9q", "zpw3jty": "z3n8v9q", "z2cp4qt": "z3n8v9q",
    "zxhktv4": "z8rxk2p", "z3gxb82": "z8rxk2p", "zcdf8mn": "z8rxk2p", "z88hcj6": "z9gm97h",
    "z22vw6f": "z9gm97h", "zxm3jty": "z9gm97h", "zyjbqhv": "zcvqrwx", "zsw3jty": "zcvqrwx",
    "zws8h39": "zgyjgdm", "zpkhcj6": "zgyjgdm", "zsqydxs": "zpmgh39", "zy7vw6f": "zpmgh39",
    "z2jydxs": "zqkpjty", "zpt4xfr": "zqkpjty", "zk3fy4j": "zsxrpbk", "z29trwx": "zxjymsg",
    "z3t4xfr": "zxjymsg", "zgh96yc": "zxjymsg", "z8c6gdm": "zxjymsg", "zyxg7p3": "zxjymsg",
    "z83qfcw": "zxjymsg", "z2rm3k7": "zyh9fcw", "z3mbqhv": "zyh9fcw", "zqqtrwx": "z2tpmsg",
    "zxtvw6f": "z2tpmsg", "z2396yc": "z34kgdm", "zwfr2nb": "z34kgdm", "zgcyw6f": "z87mw6f",
    "z8wkh39": "z87mw6f", "z3kg2nb": "z87mw6f", "ztrwng8": "z9wqk2p", "zgqhcj6": "z9wqk2p",
    "z9tvw6f": "z9wqk2p", "z96ydxs": "z9wqk2p", "zpcjsrd": "z9wqk2p", "zcsyw6f": "zcdj97h",
    "zsm7v9q": "zcdj97h", "zx98pbk": "zcdj97h", "zcjjfcw": "zcdj97h", "zdnc97h": "zg98rwx",
    "z8db7p3": "zq6h2nb", "z93jfcw": "zq6h2nb", "zyydng8": "zq6h2nb", "z8m8pbk": "zq6h2nb",
    "zcpjfcw": "zq6h2nb", "z9twsrd": "zq6h2nb", "zyhvw6f": "zs3gfcw", "z3nbqhv": "zs3gfcw",
    "z3v4xfr": "ztsyh39", "zshvw6f": "ztsyh39", "zg4qfcw": "zw2xjty", "zxy4xfr": "zw2xjty",
    "zpbkh39": "zxnftv4", "zg923k7": "zxnftv4", "z3sg2nb": "zxnftv4", "z97yw6f": "zxnftv4",
    "zg2h4qt": "zxnftv4", "zqwtcj6": "zxnftv4", "z9nr6yc": "z398rwx", "zsf9pbk": "z398rwx",
    "z2rmrwx": "z398rwx", "z2jndxs": "z398rwx", "ztr7b82": "z398rwx", "z3h4h39": "z398rwx",
    "zwhfw6f": "z3kdcj6", "z88jy4j": "z3kdcj6", "zyb4h39": "z82xjty", "zg87b82": "z82xjty",
    "z9vrjty": "zcj78mn", "zxtscj6": "zcj78mn", "zcpxfcw": "zcj78mn", "zsfpb82": "zcj78mn",
    "zpk2srd": "zcj78mn", "zxmmsrd": "zcj78mn", "zy98msg": "zcj78mn", "zgmpgdm": "zcj78mn",
    "zscrw6f": "zcj78mn", "z2ty97h": "zcj78mn", "zyd64qt": "zcwqk2p", "zwp32nb": "zcwqk2p",
    "zcgt4qt": "zp3gfcw", "z26wfcw": "zp3gfcw", "zg337p3": "zqtpmsg", "z3773k7": "zqtpmsg",
    "zgkdsrd": "zqtpmsg", "z44c4qt": "zsbry4j", "zqxyjty": "zsgcv9q", "zyg73k7": "zsgcv9q",
    "z8jt4qt": "zsgcv9q", "zgcrxfr": "zxsyh39", "zwbyjty": "zxsyh39", "zqsxrwx": "zxsyh39",
    "z8npk2p": "zxsyh39", "zg9rxfr": "zxsyh39", "z3fsdxs": "zxsyh39", "zq6vg82": "z34dycw",
    "z9jhsg8": "z34dycw", "zsgw7hv": "z34dycw", "zxsck7h": "z34dycw", "z2t3rdm": "z34dycw",
    "ztwxhv4": "zgkj39q", "zcnbcwx": "zgkj39q", "zyxsv4j": "zgkj39q", "z839dmn": "zgkj39q",
    "z3tybk7": "zgkj39q", "ztdmtyc": "zgkj39q", "z8bkwxs": "zgkj39q", "zx9qmnb": "zgkj39q",
    "zs47xsg": "zpyg6fr", "zc2sv4j": "zpyg6fr", "z2y9dmn": "zpyg6fr", "zt38j6f": "zs3chv4",
    "zqnr9qt": "zs3chv4", "zy47xsg": "zs3chv4", "z2nr9qt": "zs3chv4", "zy926fr": "zs3chv4",
    "zwt3rdm": "zs3chv4", "zc7nycw": "zs3chv4", "zcmf39q": "zts3mnb", "zyd6p39": "zts3mnb",
    "ztrj2p3": "zts3mnb", "zs926fr": "zts3mnb", "zwnr9qt": "zts3mnb", "zgd6p39": "zyg9nbk",
    "z8mf39q": "zyg9nbk", "zjrswty": "zyg9nbk", "zqbdqty": "z2tsj6f", "zt8xhv4": "z2tsj6f",
    "zcpg4j6": "z2tsj6f", "zy7nycw": "z2tsj6f", "zy2sv4j": "z2tsj6f", "z9bdqty": "z8qx4j6",
    "zq926fr": "z8qx4j6", "zp2sv4j": "z8qx4j6", "zyvygdm": "z9w2rdm", "zpphfcw": "z9w2rdm",
    "zgrg97h": "z9w2rdm", "z8d8qhv": "z9w2rdm", "z2m2tv4": "z9w2rdm", "zqrj2p3": "zqxpdmn",
    "zcnr9qt": "zqxpdmn", "z838j6f": "zw2tk7h", "zs7nycw": "zw2tk7h", "ztwtnbk": "zw2tk7h",
    "z9vkwxs": "zw2tk7h", "zgsck7h": "zw2tk7h", "zsmf39q": "zw2tk7h", "zq47xsg": "zw2tk7h",
    "z8nr9qt": "zxpy7hv", "zywtnbk": "zxpy7hv", "zwy9dmn": "zxpy7hv", "zyqpfrd": "zxpy7hv",
    "zt926fr": "zxpy7hv", "zct3rdm": "zxpy7hv", "zsd6p39": "zxpy7hv", "zxrj2p3": "zxpy7hv",
    "z8gjrdm": "z2fjp39", "zsxv6fr": "z2fjp39", "zxjpqty": "z2fjp39", "z9v839q": "z2fjp39",
    "zqc74j6": "z2fjp39", "zts3j6f": "z3df9qt", "z3d7ycw": "z3df9qt", "zpyg7hv": "z3df9qt",
    "z976g82": "z3df9qt", "zqtsk7h": "z3df9qt", "ztbdnbk": "z3wyk7h", "zxbdnbk": "z3wyk7h",
    "z3jh4j6": "z3wyk7h", "zqgwsg8": "z3wyk7h", "zsms82p": "z3wyk7h", "zppb7hv": "z3wyk7h",
    "zg2trdm": "z8642p3", "zqs3j6f": "z8642p3", "z92trdm": "z8642p3", "zxb4xsg": "z8642p3",
    "zq6n9qt": "z8642p3", "zpc8hv4": "z9mrqty", "z2s3j6f": "z9mrqty", "z8hf82p": "z9mrqty",
    "zxpydmn": "z9mrqty", "zxhf82p": "z9mrqty", "zy9wnbk": "zc7bwxs", "zsg96fr": "zc7bwxs",
    "zxfbqty": "zc7bwxs", "zg9wnbk": "zc7bwxs", "zcd7ycw": "zc7bwxs", "z82trdm": "zgjv82p",
    "zgd7ycw": "zgjv82p", "zsrktyc": "zgjv82p", "zw76g82": "zgjv82p", "z9mhcwx": "zgjv82p",
    "zq97v4j": "zgq3dmn", "ztf46fr": "zgq3dmn", "z8qp9qt": "zgq3dmn", "zwgdnbk": "zgq3dmn",
    "zpms82p": "zgq3dmn", "z347v4j": "zgq3dmn", "zk46kmn": "zh8w382", "zvyw382": "zh8w382",
    "zrb7rj6": "zh8w382", "z7jf7nb": "zh8w382", "zjdnjhv": "zh8w382", "zxcqycw": "zpr639q",
    "z2rjfrd": "zpr639q", "z27p9qt": "zpr639q", "z2w6rdm": "zpr639q", "z92s82p": "zpr639q",
    "zwscxsg": "zpr639q", "zq6m2p3": "zprysg8", "z3rb39q": "zprysg8", "ztg3v4j": "zprysg8",
    "z92qj6f": "zprysg8", "zxsphv4": "zprysg8", "zsbvycw": "zprysg8", "z9894j6": "zprysg8",
    "z8qwdmn": "zprysg8", "zgk4cwx": "zprysg8", "z9qwdmn": "zprysg8", "zxysnbk": "zprysg8",
    "ztsphv4": "zprysg8", "z3dk9qt": "zprysg8", "zw7jwxs": "zprysg8", "zcm7qty": "zprysg8",
    "z2vfsg8": "zprysg8", "zw6m2p3": "zprysg8", "zxtxmnb": "zprysg8", "z3k4cwx": "zprysg8",
    "z8txmnb": "zprysg8", "zwqp9qt": "ztbmycw", "zyrjfrd": "ztbmycw", "z9hb7hv": "ztbmycw",
    "zyy46fr": "ztbmycw", "z9cjfrd": "ztbmycw", "zswtcwx": "ztbmycw", "zpfnp39": "ztbsp39",
    "zwh6xsg": "ztbsp39", "zpbvycw": "ztbsp39", "zs4rg82": "ztbsp39", "zg8qfrd": "zwhkxsg",
    "zcmhcwx": "zwhkxsg", "zqxp4j6": "zwhkxsg", "zprktyc": "zwhkxsg", "zc2trdm": "zwhkxsg",
    "zw8s2p3": "zxv7sg8", "z22gp39": "zxv7sg8", "zpndbk7": "zxv7sg8", "zyfjrdm": "zxv7sg8",
    "ztpdbk7": "zxv7sg8", "zgqp9qt": "zykncwx", "zpgwsg8": "zykncwx", "zw7nk7h": "zykncwx",
    "z8dxg82": "zykncwx", "zp6ywxs": "zykncwx", "zxrjfrd": "zykncwx", "zt3yfrd": "z2ftxsg",
    "z82qj6f": "z2ftxsg", "zwpt6fr": "z2ftxsg", "zpcgbk7": "z2ftxsg", "zxbvycw": "z2ftxsg",
    "z2h6xsg": "z2ftxsg", "zgdk9qt": "z2ftxsg", "zg4rg82": "z2ftxsg", "z8w8k7h": "z2ftxsg",
    "zcdk9qt": "z2ftxsg", "ztysnbk": "z2ftxsg", "ztpt6fr": "z2ftxsg", "zgjd82p": "z2ftxsg",
    "z96m2p3": "z2ftxsg", "z8x27hv": "z2ftxsg", "zqm7qty": "z2ftxsg", "zw2qj6f": "z2ftxsg",
    "zqh6xsg": "z2ftxsg", "zyrb39q": "z2ftxsg", "zpysnbk": "z2ftxsg", "z8k239q": "z2swhv4",
    "zcxywxs": "z2swhv4", "z38xg82": "z2swhv4", "z8cjfrd": "z2swhv4", "zwy9tyc": "z2swhv4",
    "z8f46fr": "z2swhv4", "z9tsk7h": "z38s4j6", "zxnvwxs": "z38s4j6", "zwtsk7h": "z38s4j6",
    "zx3cmnb": "z38s4j6", "zp4dp39": "z38s4j6", "z3kmbk7": "z8xc7hv", "zwk239q": "z8xc7hv",
    "zp38p39": "z8xc7hv", "zsjh4j6": "z8xc7hv", "ztw6rdm": "z8xc7hv", "zx7v6fr": "z92gj6f",
    "z89twxs": "z92gj6f", "zys839q": "z92gj6f", "zx23tyc": "z92gj6f", "z8khj6f": "z92gj6f",
    "z39wnbk": "zgwyk7h", "zgqxbk7": "zgwyk7h", "ztb4xsg": "zgwyk7h", "zg76g82": "zgwyk7h",
    "zw2trdm": "zgwyk7h", "zpb4xsg": "zpbmycw", "z3kjsg8": "zpbmycw", "z8jm39q": "zpbmycw",
    "zc76g82": "zpbmycw", "z9qxbk7": "zpbmycw", "z2vkhv4": "zpgxv4j", "zttvj6f": "zpgxv4j",
    "zw38p39": "zpgxv4j", "zp7p9qt": "zpgxv4j", "zxvkhv4": "zpgxv4j", "zy8xg82": "zpgxv4j",
    "zht2y9q": "zpqt7p3", "z7q8t39": "zpqt7p3", "zfstgwx": "zpqt7p3", "znpx382": "zpqt7p3",
    "zsvfsg8": "zqnx2p3", "zyk4cwx": "zqnx2p3", "zqnhtyc": "zqnx2p3", "zsrb39q": "zqnx2p3",
    "z2nrmnb": "zqp86fr", "zcb8p39": "zqp86fr", "z9v9tyc": "zqp86fr", "zccjfrd": "zqp86fr",
    "z2pg2p3": "zqp86fr", "zt7p9qt": "zsctbk7", "z9wtcwx": "zsctbk7", "zygwsg8": "zsctbk7",
    "z83khv4": "zsctbk7", "zxnrmnb": "zsctbk7", "zwcjfrd": "zsctbk7", "zgkjsg8": "zsr639q",
    "zp3cmnb": "zsr639q", "z3c8hv4": "zsr639q", "zsc8hv4": "zsr639q", "z2nvwxs": "zsr639q",
    "z9xywxs": "zt32frd", "zpkmbk7": "zt32frd", "zy9239q": "zt32frd", "z26vj6f": "zt32frd",
    "zq7p9qt": "zt32frd", "zyng2p3": "zt32frd", "zc9239q": "zwt9mnb", "zgfcxsg": "zwt9mnb",
    "zy38p39": "zwt9mnb", "zptvj6f": "zwt9mnb", "z37nk7h": "zwt9mnb", "z2tsk7h": "zy4hg82",
    "z96n9qt": "zy4hg82", "z26n9qt": "zy4hg82", "zqpydmn": "zy4hg82", "ztg96fr": "zy4hg82",
    "zpvgdxs": "z2k7g82", "zpf3k2p": "z2k7g82", "z2hsrwx": "z2k7g82", "zxsv97h": "z2k7g82",
    "z826y4j": "z2k7g82", "zw7xfcw": "z2k7g82", "zpbcjty": "z2k7g82", "z8wjh39": "z2k7g82",
    "zgkw6yc": "z2k7g82", "zc8jtv4": "z2k7g82", "zx6v97h": "z388pbk", "zg42ng8": "z388pbk",
    "zgjpb82": "z388pbk", "zyy97p3": "z388pbk", "ztxv97h": "z388pbk", "z8hgdxs": "z388pbk",
    "zx82ng8": "z8bksg8", "zqrdxfr": "z8bksg8", "zcsgdxs": "z8bksg8", "zgcrjty": "z8bksg8",
    "ztj6y4j": "z8bksg8", "z3p8xfr": "z8bksg8", "z8bk2nb": "z8bksg8", "zy2pb82": "z8bksg8",
    "zcnb8mn": "z8bksg8", "z3hv97h": "z8bksg8", "zx9qh39": "z8bksg8", "z3p3k2p": "z9v4p39",
    "zsxsrwx": "zcfrtyc", "zwcw6yc": "zcfrtyc", "zxwxfcw": "zcfrtyc", "zcxsrwx": "zq4j39q",
    "zp48msg": "zq4j39q", "zpk7pbk": "zq4j39q", "z9hv97h": "zq4j39q", "zydmsrd": "zq4j39q",
    "zqfrw6f": "zq4j39q", "zc7xfcw": "zq4j39q", "z9tngdm": "zq4j39q", "zy82ng8": "zq4j39q",
    "zqpfcj6": "zq4j39q", "zcqmsrd": "zq4j39q", "zqf3k2p": "zq4j39q", "zwkpgdm": "zwrdycw",
    "z9sgdxs": "zwrdycw", "zgxsrwx": "zwrdycw", "z9387p3": "z3hv2p3", "z3hb97h": "z3hv2p3",
    "zpmfgdm": "z3hv2p3", "z9vkqhv": "z3hv2p3", "zw47tv4": "z3hv2p3", "zc62srd": "z3hv2p3",
    "z36vcj6": "z3hv2p3", "zy6vcj6": "z3hv2p3", "zpjhy4j": "z3hv2p3", "z8y9jty": "z3hv2p3",
    "z9y9jty": "z3hv2p3", "zp2sb82": "z3hv2p3", "zgqpv9q": "zgnbxsg", "zxy9jty": "zgnbxsg",
    "zpn87p3": "zgnbxsg", "zscq6yc": "zgnbxsg", "z9hb97h": "zgnbxsg", "zpkmpbk": "zgnbxsg",
    "z3kmpbk": "zgnbxsg", "z8scdxs": "zgnbxsg", "ztkmpbk": "zgnbxsg", "zg6vcj6": "zgnbxsg",
    "zsrq6yc": "zpqtk7h", "z3jpv9q": "zqyyw6f", "zydtfcw": "zqyyw6f", "z8hgk2p": "zqyyw6f",
    "zwpr8mn": "zqyyw6f", "zxbwmsg": "zqyyw6f", "zqjhy4j": "zs2pdmn", "zx2sb82": "zs2pdmn",
    "zgbd2nb": "zs2pdmn", "z8myrwx": "zs2pdmn", "zcwhy4j": "zs2pdmn", "zsgjxfr": "zs2pdmn",
    "z3c7tv4": "zs2pdmn", "zshb97h": "zs2pdmn", "zt6vcj6": "zs2pdmn", "ztf9jty": "zs2pdmn",
    "z9jpv9q": "zs2pdmn", "zwhgk2p": "ztwx4j6", "zwtb97h": "ztwx4j6", "zc7sb82": "ztwx4j6",
    "zpxyrwx": "zyxsj6f", "zqd6srd": "zyxsj6f", "z9rjxfr": "zyxsj6f", "z2wh3k7": "z39ry4j",
    "zc3dxfr": "z39ry4j", "z8c7pbk": "z39ry4j", "z3s4qhv": "z39ry4j", "zpqngdm": "z82j97h",
    "ztjpb82": "z82j97h", "zwc7pbk": "z82j97h", "z93dxfr": "z82j97h", "zp2fcj6": "z82j97h",
    "zgncjty": "z82j97h", "z9v8msg": "z82j97h", "zyxv97h": "z82j97h", "zytb8mn": "z82j97h",
    "z9bw6yc": "zcwkgdm", "z2dtv9q": "zcwkgdm", "zw42ng8": "zcwkgdm", "zt7srwx": "zcwkgdm",
    "zs63k2p": "zcwkgdm", "zgf97p3": "zcwkgdm", "zpdtv9q": "zp3ftv4", "z9s4qhv": "zp3ftv4",
    "z3xv97h": "zp3ftv4", "z83dxfr": "zqtmw6f", "zxkxfcw": "zqtmw6f", "zx86y4j": "zqtmw6f",
    "z3tb8mn": "zqtmw6f", "zpjpb82": "zqtmw6f", "zpxv97h": "zsbyh39", "zt2fcj6": "zsbyh39",
    "zstb8mn": "zsbyh39", "zd872nb": "ztfpmsg", "zqjgtv4": "ztfpmsg", "zqrqh39": "zxsh2nb",
    "zsqngdm": "zxsh2nb", "zcncjty": "zxsh2nb", "zchgdxs": "zycbsrd", "z8hsrwx": "zycbsrd",
    "z2gjtv4": "zycbsrd", "zp8jtv4": "zycbsrd", "znd72nb": "z3qdcj6", "zymy97h": "z8p6qhv",
    "z242srd": "z8p6qhv", "zpjpgdm": "z8p6qhv", "ztkxy4j": "z9hxjty", "zsjpgdm": "z9hxjty",
    "z3dt3k7": "z9p6qhv", "z9ykmsg": "zcx78mn", "zgprjty": "zcx78mn", "z3xvk2p": "zgmqk2p",
    "zcprjty": "zgmqk2p", "zqs47p3": "zgx78mn", "zprqpbk": "zgx78mn", "zx3d6yc": "zgx78mn",
    "zs9mfcw": "zgx78mn", "z3whb82": "zgx78mn", "zx9mfcw": "zp9ry4j", "zctbdxs": "zqvs6yc",
    "zq3d6yc": "zqvs6yc", "zyqnrwx": "zqvs6yc", "zp86v9q": "zqvs6yc", "zwbwtv4": "zqynxfr",
    "z9f92nb": "zqynxfr", "z9638mn": "zsd9b82", "zydt3k7": "zsd9b82", "zg2f4qt": "zsd9b82",
    "zwf92nb": "zt4gfcw", "zs86v9q": "zt4gfcw", "zc638mn": "zt4gfcw", "z9ncqhv": "zwfpmsg",
    "zwv8xfr": "zwfpmsg", "zg638mn": "zwfpmsg", "z3638mn": "zxgvpbk", "zsqnrwx": "zxgvpbk",
    "z2bwtv4": "zxr3ng8", "zt42srd": "zxr3ng8", "z32f4qt": "zxr3ng8", "z8ykmsg": "zywkgdm",
    "zqgjh39": "zywkgdm"
}


def get_study_guide_id_list(topic_ids):
    dictionary = {}

    for topic_id in topic_ids:
        try:
            dictionary[topic_id] = STUDY_GUIDES_IDS_PER_TOPIC_ID[topic_id]
        except KeyError:
            raise Exception(
                f'[NOT FOUND]: No studyGuideIds found for topicId: {topic_id}')

    return list(itertools.chain(*dictionary.values()))


def get_topic_id(study_guide_ids):
    dictionary = {}

    for study_guide_id in study_guide_ids:
        try:
            dictionary[study_guide_id] = TOPIC_ID_PER_STUDY_GUIDE_ID[study_guide_id]
        except KeyError:
            raise Exception(
                f'[NOT FOUND]: No topicId found for studyGuideId: {study_guide_id}')

    return dictionary
