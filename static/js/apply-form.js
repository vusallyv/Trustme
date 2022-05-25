$(document).ready(function () {
    if (document.querySelector("#applyModal")) {
        $('.modal-select').select2({
            dropdownParent: $('#applyModal'),
            placeholder: gettext("Xidmət seçin"),
        });
    }

    if (document.querySelector("#applyModal"))  {
        $(".prefix").select2({
            templateResult: formatState2,
            templateSelection: formatState,
            dropdownParent: $('#applyModal')
        });
    } else {
        $(".prefix").select2({
            templateResult: formatState2,
            templateSelection: formatState,
        });
    }


    if (document.querySelector("#standartPacketModal")) {
        $(".prefix-standartPacket").select2({
            templateResult: formatState2,
            templateSelection: formatState,
            dropdownParent: $('#standartPacketModal')
        });
    }

    if (document.querySelector("#premiumPacketModal")) {
        $(".prefix-premiumPacket").select2({
            templateResult: formatState2,
            templateSelection: formatState,
            dropdownParent: $('#premiumPacketModal')
        });
    }

    if (document.querySelector("#platinumPacketModal")) {
        $(".prefix-platinumPacket").select2({
            templateResult: formatState2,
            templateSelection: formatState,
            dropdownParent: $('#platinumPacketModal')
        });
    }
});

let icons = {
    "+994": "./static/assets/svg/flag.svg",
    "+7": "./static/assets/img/russia-flag.png",
    "+1": "./static/assets/img/usa-flag.png"
}

function formatState(state) {
    if (!state.id) { return state.text; }
    var $state = $(
        `
        <div class="prefix-wrapper" 
        style="border-radius: 0.25rem;
        display: flex;
        align-items: center;
        gap: 0.4375rem;">
        <img src="${icons[state.text]}"
        style="width: 15px; 
        border-radius: 50%;
        height: 15px;"/>
        <span 
        style="display: flex;
        align-items: center;
        gap: 0.3125rem;
        font-size: .8125rem;">
          ${state.text}
          <img src="./static/assets/svg/down.svg" />
        </span>
        </div>
        `
    );
    return $state;
}

function formatState2(state) {
    if (!state.id) { return state.text; }
    var $state = $(
        `
        <div class="prefix-wrapper" 
        style="border-radius: 0.25rem;
        display: flex;
        align-items: center;
        gap: 0.3125rem;">
        <img src="${icons[state.text]}" 
        style="width: 15px; 
        border-radius: 50%;
        height: 15px;"/>
        <span 
        style="display: flex;
        align-items: center;
        gap: 0.3125rem;
        font-size: .8125rem;">
          ${state.text}
        </span>
        </div>
        `
    );
    return $state;
}