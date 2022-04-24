class Category:
    detail = {
        "marriage1": {"select": "求婚花束", "type": "marriage", "alt": "求婚花束", "path": "/static/img/products/marriage/soap7/", "price": "$700", "description": "7朵玫瑰", "size": "花面寬約30cm(含包裝)、總長約40cm"},
        "marriage2": {"select": "求婚花束", "type": "marriage", "alt": "求婚花束", "path": "/static/img/products/marriage/soap9/", "price": "$890", "description": "9朵玫瑰", "size": "花面寬約35cm(含包裝)、總長約50cm"},
        "marriage3": {"select": "求婚花束", "type": "marriage", "alt": "求婚花束", "path": "/static/img/products/marriage/soap12/", "price": "$1200", "description": "12朵玫瑰", "size": "花面寬約45cm(含包裝)、總長約60cm"},
        "dryflower1": {"select": "乾燥花束", "type": "dryflower", "alt": "乾燥花束", "path": "/static/img/products/dryflower/", "price": "$250", "description": "", "size": "花面寬約10cm(含包裝)、總長約25cm"},
        "dryflower2": {"select": "乾燥花束", "type": "dryflower", "alt": "乾燥花束", "path": "/static/img/products/dryflower/", "price": "$299", "description": "", "size": "花面寬約15cm(含包裝)、總長約30cm"},
        "dryflower3": {"select": "乾燥花束", "type": "dryflower", "alt": "乾燥花束", "path": "/static/img/products/dryflower/", "price": "$500", "description": "", "size": "花面寬約23cm(含包裝)、總長約35cm"},
        "glass1": {"select": "玻璃盅罩", "type": "glass", "alt": "玻璃罩", "path": "/static/img/products/glass/", "price": "$1200", "description": "盅罩有燈款", "size": "外徑14cm、內徑10.5cm、總高約16.5cm"},
        "glass2": {"select": "玻璃盅罩", "type": "glass", "alt": "玻璃罩", "path": "/static/img/products/glass/", "price": "$690", "description": "盅罩無燈款", "size": "外徑10.4cm、內徑7cm、總高約15cm"},
        "glass3": {"select": "玻璃盅罩", "type": "glass", "alt": "玻璃罩", "path": "/static/img/products/glass/", "price": "$800", "description": "圓罩無燈款", "size": "外徑11.3cm、內徑8cm、總高約10cm"},
        "glass4": {"select": "玻璃盅罩", "type": "glass", "alt": "玻璃罩", "path": "/static/img/products/glass/", "price": "860", "description": "圓罩有燈款", "size": "外徑11.3cm、內徑8cm、總高約12cm"},
        "decoration1": {"select": "裝飾小物", "type": "decoration", "alt": "相框", "path": "/static/img/products/decoration/", "price": "720", "description": "方形框", "size": "19.5X19.3cm"},
        "decoration2": {"select": "裝飾小物", "type": "decoration", "alt": "相框", "path": "/static/img/products/decoration/", "price": "560", "description": "矩形框", "size": "19.5X14.4cm"}
    }
    all = {
        "newtype": {"title": "最新創作","url": "/category?onseason=newtype", },
        "classictype": {"title": "經典不敗","url": "/category?onseason=classictype", },
        "graduate": {"title": "畢業花束","url": "/category?type=graduate", "src": "/static/img/products/glass/S__88014851", "alt": "畢業花束", },
        "mother": {"title": "母親節花束","url": "/category?type=mother", "src": "/static/img/products/glass/S__88014851", "alt": "母親節花束", },
        "marriage": {"title": "求婚花束","url": "/category?type=marriage", "src": "/static/img/category/LINE_ALBUM_$7007朵玫瑰_220405_0", "alt": "求婚花束", },
        "dryflower": {"title": "乾燥花束","url": "/category?type=dryflower", "src": "/static/img/category/LINE_ALBUM_$299花束_220423_1", "alt": "乾燥花束", },
        "glass": {"title": "玻璃盅罩","url": "/category?type=glass", "src": "/static/img/category/LINE_ALBUM_玻璃盅罩_220423_0", "alt": "玻璃罩", },
        "decoration": {"title": "裝飾小物","url": "/category?type=decoration", "src": "/static/img/category/LINE_ALBUM_花圈_220423_7", "alt": "婚禮小物", },
        "wedding": {"title": "婚禮系列","url": "/category?type=wedding", "src": "/static/img/category/LINE_ALBUM_捧花_220423_0", "alt": "婚禮捧花", },
        "plants": {"title": "盆花花禮","url": "/category?type=plants", "src": "/static/img/category/LINE_ALBUM_花禮盆器_220423_0", "alt": "乾燥花盆花", }
    }
    inIndex=["graduate","mother","marriage","dryflower","glass","decoration","wedding","plants"]


class SideBar:
    detail=["mother","marriage","dryflower","glass","wedding","plants"]
    only=["newtype","classictype"]

class HomePage:
    news={
        "title":"謝謝媽咪!",
        "paragarph":"「小時候最想做的事是快快長大，而長大後最希望的事是你慢慢變老。」",
        "src":"",
        "url":"",
        "alt":"",
    }
    onseason={
        "title":"母親節最新款",
        "paragraph":"",
        "src":"",
        "url":"",
        "alt":"",
    }

class Precaution:
    items={
        "needTime":{
            "title":"製作及運送時間",
            "content":{"下單製作工作天約3~5天","寄送時間約2~3天(不含離島)","小件單一商品可超取 運費$60","大件單一商品需郵寄 高雄市運費$70 外縣市運費$80 離島另計"},
            "caution":"下單前請留意，急單請私訊或來電洽詢"
        },
        "material":{
            "title":"使用的花材及包材",
            "content":
            {"主花配置都會與圖片相符(若有特殊狀況會事先跟顧客協調!)，配花的部分會依當季或現有的花材搭配，花藝師會依專業地的配置整體美感，若有疑慮請三思喔!",
            "包材會儘量配置與圖片中相符，會依現有的去做相似搭配，有疑慮的話請三思!",
            "若有特殊需求請事先告知、溝通(EX:希望配花有滿天星、繡球……、緞帶顏色希望紅色…等等)，作品完成後比較無法更改。"},
            "caution":"下單前請留意，若有疑慮請勿下單"
        },
        "printCard":{
            "title":"卡片打印",
            "content":{"需事先提供內容，我們會編排、列印","若有特殊需求請事先告知(EX:字體顏色、要加表情符號、字體大小要均一)，無事先告知視同相信我們的編排，編輯後無法更改喔!","卡片背景為固定格式，無法挑選"},
            "caution":"請詳讀，卡片無法來回更改"
        }
    }


