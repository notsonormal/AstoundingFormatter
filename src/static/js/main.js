$(document).ready(function() {
	
	 $('#format-xml').click(function() {
	 	
	 	$('#format-xml').attr("disabled", true);
	 	//$('#copy-to-clipboard').attr("disabled", true);
	 	
	 	$.post('/format', { 
	 		'xml': $('#xml-textarea').val(),
	 		'fixupXml': $('#fixup-xml').is(':checked')
	 	}, function(data) {	 		
	 		
	 		$('#format-alert').alert('close');
 	 		if (data != null && data.length > 0) {
	 			$('#xml-textarea').val(data);
	 			$('#xml-textarea').scrollLeft(0);
 	 		} 	 	 		 			 	
	 	}).fail(function(req, status, error) {
	 		
	 		if ('console' in self && 'log' in console)	 			 	
	 			console.log(req.responseText);
	 		
	 		$('#format-alert').alert();
	 	}).always(function() {
	 		$('#format-xml').attr("disabled", false);
	 		//$('#copy-to-clipboard').attr("disabled", false);	 		 	
	 	});
	 	
	 	//return true;
	 });
	 
	 //$('#copy-to-clipboard').zclip({
	 //	path: '/js/ZeroClipboard.swf',
	 //	copy: function() { 
	 //		alert("COPY");
	 //		return $('textarea#xml-textarea').val(); 
	 //	}
	 //});
});