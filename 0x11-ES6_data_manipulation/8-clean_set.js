export default function cleanSet (set, startString) {
	len_ss = startString.length();
	let s = '';
	set.foreach(item =>{if(item.startsWith(startString)) s = s  + item.slice(len_ss) + '-'});
	return s.slice(0, s.length -1);
}
