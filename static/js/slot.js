let domain = "http://127.0.0.1:8000";
class Slot {
  constructor(slot) {
    this.slotId = slot.data("slot");
    this.bookBtn = slot.find(".bookBtn");
    this.bookBtn.on("click", this.handelbookBtnClick);
  }
  handelbookBtnClick = () => {
    let url = `${domain}/appointments/api/`;
    createApi(url, this.slotId);
  };
}

$(".slots").each(function () {
  let newSlot = new Slot($(this));
});
