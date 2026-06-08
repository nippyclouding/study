//지도를 담을 영역의 DOM 레퍼런스
var container = document.getElementById('map');
var options = {
    //지도를 생성할 때 필요한 기본 옵션
    center: new kakao.maps.LatLng(33.450701, 126.570667), //지도의 중심좌표.
    level: 3 //지도의 레벨(확대, 축소 정도)
};

var map = new kakao.maps.Map(container, options); //지도 생성 및 객체 리턴







// --- 여기서부터 확장팩(services 라이브러리) 사용 예시 ---
// 1. 주소-좌표 변환 객체(Geocoder)를 생성합니다.
var geocoder = new kakao.maps.services.Geocoder();

// 2. 주소로 좌표를 검색합니다. (카카오 본사 주소 예시)
geocoder.addressSearch('제주특별자치도 제주시 첨단로 242', function (result, status) {

    // 정상적으로 검색이 완료됐으면 (상태가 OK이면)
    if (status === kakao.maps.services.Status.OK) {
        // 찾은 결과에서 좌표값을 뽑아냅니다.
        var coords = new kakao.maps.LatLng(result[0].y, result[0].x);

        // 그 위치에 마커(빨간 핀)를 꽂습니다.
        var marker = new kakao.maps.Marker({
            map: map,
            position: coords
        });

        // 인포윈도우(말풍선)로 장소에 대한 설명을 표시합니다.
        var infowindow = new kakao.maps.InfoWindow({
            //content: '<div style="width:150px;text-align:center;padding:6px 0;font-weight:bold;">카카오 본사 🏢</div>'
            // 위도(y)와 경도(x)를 연결해서 카카오맵 길찾기 URL을 만듭니다.
            content: '<div style="width:150px;text-align:center;padding:10px 0;">' +
                '  <b>카카오 본사 🏢</b><br>' +
                '  <a href="https://map.kakao.com/link/to/카카오본사,' + result[0].y + ',' + result[0].x + '" target="_blank" style="color:blue; text-decoration:none;">' +
                '    🚗 길찾기 바로가기' +
                '  </a>' +
                '</div>'

        });

        // 말풍선을 마커 위에 엽니다.
        infowindow.open(map, marker);

        // 지도의 중심을 우리가 찾은 주소 위치로 이동시킵니다!
        map.setCenter(coords);
    }
});