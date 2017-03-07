let get_name_questions = function() {
    let a = $("input#name").val()
    let b = $("textarea#question").val()
    return {'name': a,
            'question': b}
};

let send_coefficient_json = function(name_question) {
    $.ajax({
        url: '/solve',
        contentType: "application/json; charset=utf-8",
        type: 'POST',
        success: function (data) {
            display_solutions(data);
        },
        data: JSON.stringify(name_question)
    });
};

let display_solutions = function(solutions) {
    $("span#solution").html(solutions.answer)
};


$(document).ready(function() {

    $("button#solve").click(function() {
        let info = get_name_questions();
        send_coefficient_json(info);
    })

})
