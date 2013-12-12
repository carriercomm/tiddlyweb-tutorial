
(function($) {
	var uri = '/bags/system/tiddlers',
		bagUri = '/bags/newbag',
        content = $('#content'),
		bagInfo = $('#bag');



	function displayTiddlerInfo(data) {
		$.each(data, function(index, tiddler) {
			content.append('<li>' + tiddler.title + '</li>');
		});
	}

	function displayBagInfo(data) {
		var desc = data.desc,
            policy = data.policy,
			list = $('<dl>');

		bagInfo.append('desc');
		$.each(policy, function(key, value) {
			list.append('<dt>' + key + '</dt>');
			list.append('<dd>' + value + '</dd>');
		});
		bagInfo.append(list);
	}

	$.ajax({
		url: uri,
		dataType: 'JSON',
		success: displayTiddlerInfo
	});

	$.ajax({
		url: bagUri,
		dataType: 'JSON',
		success: displayBagInfo
	});
}(jQuery));
