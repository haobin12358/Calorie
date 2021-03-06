import wepy from 'wepy';

//  拿到windowHeight后设置合适的cardHeight
export default class CardMixin extends wepy.mixin {
  props = {
    xxx: {
      //  Object Array String Number Boolean
      type: Object
    }
  };

  data = {
    containerHeight: 0,
    cardHeight: 0
  };

  computed = {};

  methods = {};

  events = {};

  onLoad() {
    let sysInfo = wx.getSystemInfoSync();

    this.cardHeight = sysInfo.windowHeight * 0.9;
    this.containerHeight = sysInfo.windowHeight;
  }
}

