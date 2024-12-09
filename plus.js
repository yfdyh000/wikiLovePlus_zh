//mw.loader.using('ext.wikiLove.defaultOptions', function() { // 浏览器调试运行时注释此句
  function csvToObject(csvString) {
    const lines = csvString.trim().split('\n');
    const result = [];
    for (const line of lines) {
        if (line.trim() == "") continue;
        const values = line.split(',');
        const keyName = values[0];
        const obj = {
            fields: ['header', 'message'],
            option: values[0],
            header: values[2],
            title: values[2],
            image: values[1],
            imageSize: '200px',
        };
        result[keyName] = obj;
    }
    return result;
  }

  const items_huabei = csvToObject(`北京烤鸭,Roasted_Beijing_Duck_sliced.jpg,北京烤鸭送给您！
  炸酱面,"Taste_of_Beijing,_Soho,_London_(4363231155).jpg",请您吃老北京炸酱面！
  煎饼果子,Jianbing_being_prepared.jpg,煎饼果子送给您！
  炒栗子,Roastedchestnut.jpg,炒栗子送给您！
  驴肉火烧,"Donkey_sandwich,_Baoding_style_(20160310111719).jpg",驴肉火烧送给您！
  四喜丸子,Sixi_Balls.png,四喜丸子送给您！
  德州扒鸡,Single_Dezhou_braised_chicken_wrapped_in_paper_(20170115132902).jpg,送您一只德州扒鸡！
  葱烧海参,Braised_Guandong_Sea_Cucumber_with_Scallion_in_Sauce.jpg,葱烧海参送给您！
  九转大肠,Jiuqu_dachang_2009_03.jpg,九转大肠送给您！
  拔丝地瓜,拔丝地瓜.jpg,拔丝地瓜送给您！
  韭菜盒子,韭菜盒.jpg,送您一盘韭菜盒子！`);
  const items_dongbei = csvToObject(`饺子,Cuisine_of_China_0053.JPG,一盘饺子送给您！
  红肠,Smoked_Chinese_sausage.jpg,哈尔滨红肠送给您！
  锅包肉,Guōbāoròu.jpg,锅包肉送给您！`);
  const items_jiangnan = csvToObject(`
  小笼包,Xiaolongbao_Shanghai.jpg,一笼小笼包送给您！
  扬州炒饭,"Chinese_fried_rice_by_stu_spivack_in_Cleveland,_OH.jpg",扬州炒饭送给您！
  东坡肉,BCfood12.JPG,一钵东坡肉送给您！
  龙井虾仁,Longjing_prawns_in_Hangzhou_Restaurant_2015-07.JPG,来吃龙井虾仁！
  红烧狮子头,Lions-head-MCB.jpg,红烧狮子头请您吃！
  叫化鸡,Beggar's_Chicken_(_叫化雞).jpg,送您一只叫化鸡！
  贵池小粑,贵池早市_小粑.jpg,一个贵池小粑送给您！`);

    const items_chinese = {
        tieguanyin: {
          fields: [ 'header', 'message' ],
          option: '铁观音',
          header: '铁观音茶送给您！',
          title: '铁观音茶送给您！',
          image: 'Tieguanyin2.jpg',
          imageSize: '200px'
        },
        spicy_gluten: {
          fields: [ 'header', 'message' ],
          option: '辣条',
          header: '辣条送给您！',
          title: '辣条送给您！',
          image: 'Spicy_gluten.png',
          imageSize: '200px'
        },
        manchu_han: {
          fields: [ 'header', 'message' ],
          option: '满汉全席',
          header: '一份满汉全席大餐送给您！',
          title: '一份满汉全席大餐送给您！',
          image: 'Manchu_Han_Imperial_Feast_Tao_Heung_Museum_of_Food_Culture.jpg',
          imageSize: '200px'
        },
        youtiao: {
          fields: [ 'header', 'message' ],
          option: '油条',
          header: '油条送给您！',
          title: '油条送给您！',
          image: 'Youtiao.jpg',
          imageSize: '200px'
        },
        bingtanghulu: {
          fields: [ 'header', 'message' ],
          option: '冰糖葫芦',
          header: '冰糖葫芦送给您！',
          title: '冰糖葫芦送给您！',
          image: 'Bthl.jpg',
          imageSize: '200px'
        },
        wotou: {
          fields: [ 'header', 'message' ],
          option: '窝头',
          header: '窝窝头送给您！',
          title: '窝窝头送给您！',
          image: '窝窝头_(7376312092).jpg',
          imageSize: '200px'
        },
        dazhaxie: {
          fields: [ 'header', 'message' ],
          option: '大闸蟹',
          header: '送您一盘大闸蟹！',
          title: '送您一盘大闸蟹！',
          image: 'Gekochte_Wollhandkrabben.jpg',
          imageSize: '200px'
        },
        zhacai: {
          fields: [ 'header', 'message' ],
          option: '榨菜',
          header: '榨菜送给您！',
          title: '榨菜送给您！',
          image: 'TwoHeadsZhacai.jpg',
          imageSize: '200px'
        },
        tea_egg: {
          fields: [ 'header', 'message' ],
          option: '茶叶蛋',
          header: '送您一颗茶叶蛋！',
          title: '送您一颗茶叶蛋！',
          image: 'TeaEgg.jpg',
          imageSize: '200px'
        }
      };

  $.wikiLoveOptions.types.chineseFood = { // 除二次定制外部调用外，变量名称不重要
    name: '中式特色饮食',
    select: '选择一种饮食：',
    subtypes: items_chinese,
    icon: 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/78/Youtiao.jpg/50px-Youtiao.jpg'
  };
  $.wikiLoveOptions.types.huabeiFood = {
    name: '中国华北饮食',
    select: '选择一种饮食：',
    subtypes: items_huabei,
    icon: 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/78/Youtiao.jpg/50px-Youtiao.jpg' // 以下暂未修改
  };
  $.wikiLoveOptions.types.dongbeiFood = {
    name: '中国东北饮食',
    select: '选择一种饮食：',
    subtypes: items_dongbei,
    icon: 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/78/Youtiao.jpg/50px-Youtiao.jpg'
  };
  $.wikiLoveOptions.types.jiangnanFood = {
    name: '中国江南饮食',
    select: '选择一种饮食：',
    subtypes: items_jiangnan,
    icon: 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/78/Youtiao.jpg/50px-Youtiao.jpg'
  };
//} ); // 见第一行