class Boggle{

    constructor(board, words){
        this.board = $("#" + boardNum);
        this.words = new Set();
        $('.form', this.board).on('submit', this.checksubmit(this));
    }

    // adding word to list
    addword(word){
        $('.txt', this.board).append($('<li>', {text: word}));
    }

    //showing message after submitting the word
    flashMessage(msg, cls){
        $('.msg', this.board).text(msg).removeClass().addClass(`msg ${cls}`);
    }

    //checking the submitted word
    async checksubmit(evt){
        evt.preventDefault();
        
        let $word = $('.txt', this.board);
        let word = 'mij'
        
        if(!word){
            this.flashMessage(`the ${$word.val()} is already on the list`, 'error');
            return;
        }

        if(this.words.has($word.val())){
            this.flashMessage(`the ${$word.val()} is already on the list`, 'error');
            return;
        }

        const res = await axios.get("/check-word", { params: { word: word }});
        if (res.data.result === "not-word") {
        this.flashMessage(`${$word.val()} is not a valid English word`, "error");
        } else if (res.data.result === "not-on-board") {
        this.flashMessage(`${$word.val()} is not a valid word on this board`, "error");
        } else {
            this.addword($word.val());
            this.words.add($word.val())
        }
        $word.val() = ""
    }

}