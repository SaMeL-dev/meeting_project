# meeting_app/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q, Count
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from django.utils import timezone
from .models import *
from .forms import *
import json

<<<<<<< HEAD
def 클래스검색및신청(request):
    """클래스(소모임) 검색 및 신청 화면"""
    try:
        # 기본 검색 폼
        form = ClassSearchForm(request.GET or None)
        
        # 모든 클래스 조회
        classes = Class.objects.all().annotate(
            member_count=Count('sugang_set', distinct=True)
        ).order_by('-classID')
        
        # 페이지네이션
        paginator = Paginator(classes, 12)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        
        # 통계 데이터
        total_classes = Class.objects.count()
        total_members = Member.objects.count()
        total_interests = Interests.objects.count()
        total_participants = 0
        
        context = {
            'form': form,
            'classes': page_obj,
            'current_category': 'all',
            'current_sort': 'recent',
            'total_classes': total_classes,
            'total_members': total_members,
            'total_interests': total_interests,
            'total_participants': total_participants,
            'popular_interests': [],
        }
        
        return render(request, 'class_search.html', context)
        
    except Exception as e:
        print(f"Error in 클래스검색및신청: {e}")
        return render(request, 'class_search.html', {
            'form': ClassSearchForm(),
            'classes': [],
            'current_category': 'all',
            'current_sort': 'recent',
            'total_classes': 0,
            'total_members': 0,
            'total_interests': 0,
            'total_participants': 0,
            'popular_interests': [],
        })

=======
>>>>>>> 5a4edcb6a4c3843af1a3137a75cee3f06ca8229b
def 로그인(request):
    """로그인 화면"""
    if request.method == 'POST':
        account_id = request.POST.get('accountID')
        password = request.POST.get('password')
        
        try:
            member = Member.objects.get(accountID=account_id, password=password)
            request.session['member_id'] = member.accountID
            messages.success(request, f'{member.name}님 환영합니다!')
            return redirect('classes')
        except Member.DoesNotExist:
            messages.error(request, '아이디 또는 비밀번호가 잘못되었습니다.')
    
    return render(request, 'login.html')

def 로그아웃(request):
    """로그아웃"""
    if 'member_id' in request.session:
        del request.session['member_id']
    messages.success(request, '로그아웃되었습니다.')
    return redirect('login')

def 회원가입(request):
    """회원 가입 화면"""
    if request.method == 'POST':
        form = MemberRegistrationForm(request.POST)
        if form.is_valid():
<<<<<<< HEAD
            try:
                member = form.save()
                messages.success(request, '회원가입이 완료되었습니다.')
                return redirect('login')
            except Exception as e:
                messages.error(request, f'회원가입 중 오류가 발생했습니다: {str(e)}')
=======
            # 이메일 중복 확인
            if Member.objects.filter(email=form.cleaned_data['email']).exists():
                messages.error(request, '이미 사용 중인 이메일입니다.')
                return render(request, 'register.html', {'form': form})
            
            member = form.save()
            messages.success(request, '회원가입이 완료되었습니다.')
            return redirect('login')
>>>>>>> 5a4edcb6a4c3843af1a3137a75cee3f06ca8229b
    else:
        form = MemberRegistrationForm()
    
    return render(request, 'register.html', {'form': form})

<<<<<<< HEAD
@require_POST
=======
def 클래스검색및신청(request):
    """클래스(소모임) 검색 및 신청 화면"""
    try:
        print("=== DEBUG: 클래스검색및신청 함수 시작 ===")
        
        # 검색 폼
        form = ClassSearchForm(request.GET)
        
        # 기본 쿼리셋
        classes = Class.objects.select_related('interestID').annotate(
            member_count=Count('sugang_set', distinct=True)
        )
        
        print(f"DEBUG: 전체 클래스 수: {classes.count()}")
        
        # 카테고리별 필터링
        category = request.GET.get('category', 'all')
        keyword = request.GET.get('keyword', '')
        
        print(f"DEBUG: category={category}, keyword={keyword}")
        
        # 카테고리 매핑
        category_keywords = {
            'sports': ['테니스', '배드민턴', '축구', '농구', '야구', '배구', '수영', '요가', '필라테스', 
                      '헬스', '크로스핏', '러닝', '마라톤', '등산', '트레킹', '클라이밍', '골프', '볼링'],
            'study': ['영어', '중국어', '일본어', 'Java', 'Python', '토익', '토플', '독서', 
                     '프로그래밍', '투자', '주식', '경제', '스터디', '공부'],
            'hobby': ['요리', '베이킹', '커피', '와인', '여행', '게임', '카페', '맛집', '쇼핑', '패션'],
            'culture': ['영화', '연극', '뮤지컬', '콘서트', '음악', '미술', '사진', '전시회', '갤러리'],
            'lifestyle': ['반려동물', '원예', '인테리어', '명상', '힐링', '아로마', '자원봉사']
        }
        
        # 카테고리 필터링
        if category != 'all' and category in category_keywords:
            keywords = category_keywords[category]
            interest_filter = Q()
            for kw in keywords:
                interest_filter |= Q(interestID__interestName__icontains=kw)
            classes = classes.filter(interest_filter)
            print(f"DEBUG: 카테고리 필터 후 클래스 수: {classes.count()}")
        
        # 키워드 검색
        search_keyword = keyword or request.GET.get('search', '')
        if search_keyword:
            classes = classes.filter(
                Q(className__icontains=search_keyword) |
                Q(interestID__interestName__icontains=search_keyword)
            ).distinct()
            print(f"DEBUG: 키워드 검색 후 클래스 수: {classes.count()}")
        
        # 검색 폼 처리
        if form.is_valid():
            form_keyword = form.cleaned_data.get('keyword')
            interest = form.cleaned_data.get('interest')
            
            if form_keyword:
                classes = classes.filter(
                    Q(className__icontains=form_keyword) |
                    Q(interestID__interestName__icontains=form_keyword)
                ).distinct()
            
            if interest:
                classes = classes.filter(interestID=interest)
        
        # 정렬
        sort_by = request.GET.get('sort', 'recent')
        if sort_by == 'popular':
            classes = classes.order_by('-member_count', '-classID')
        elif sort_by == 'name':
            classes = classes.order_by('className')
        else:
            classes = classes.order_by('-classID')
        
        # 페이지네이션
        paginator = Paginator(classes, 12)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        
        # 통계 데이터 계산
        total_classes = Class.objects.count()
        total_members = Member.objects.count()
        total_interests = Interests.objects.count()
        total_participants = Sugang.objects.values('member_accountID').distinct().count()
        
        print(f"DEBUG: 통계 - 클래스:{total_classes}, 회원:{total_members}, 관심사:{total_interests}, 참여자:{total_participants}")
        
        # 인기 관심사
        popular_interests = Interests.objects.annotate(
            class_count=Count('classes', distinct=True)
        ).filter(class_count__gt=0).order_by('-class_count')[:10]
        
        context = {
            'form': form,
            'classes': page_obj,
            'current_category': category,
            'current_sort': sort_by,
            'current_keyword': search_keyword,
            'total_classes': total_classes,
            'total_members': total_members,
            'total_interests': total_interests,
            'total_participants': total_participants,
            'popular_interests': popular_interests,
        }
        
        print(f"DEBUG: context 데이터 확인 완료")
        return render(request, 'class_search.html', context)
        
    except Exception as e:
        print(f"DEBUG: Error in 클래스검색및신청: {e}")
        import traceback
        traceback.print_exc()
        
        # 오류 발생 시 기본 데이터
        context = {
            'form': ClassSearchForm(),
            'classes': Class.objects.none(),
            'current_category': 'all',
            'current_sort': 'recent', 
            'current_keyword': '',
            'total_classes': Class.objects.count(),
            'total_members': Member.objects.count(),
            'total_interests': Interests.objects.count(),
            'total_participants': 0,
            'popular_interests': [],
        }
        return render(request, 'class_search.html', context)

@require_POST 
>>>>>>> 5a4edcb6a4c3843af1a3137a75cee3f06ca8229b
@csrf_exempt
def 클래스신청(request, class_id):
    """클래스 신청 처리"""
    if 'member_id' not in request.session:
        return JsonResponse({'success': False, 'message': '로그인이 필요합니다.'})
    
    try:
        member = get_object_or_404(Member, accountID=request.session['member_id'])
        클래스 = get_object_or_404(Class, classID=class_id)
        
        # 이미 신청했는지 확인
        if Sugang.objects.filter(member_accountID=member, class_classID=클래스).exists():
            return JsonResponse({'success': False, 'message': '이미 신청한 클래스입니다.'})
        
        # 수강 신청
        Sugang.objects.create(member_accountID=member, class_classID=클래스)
        return JsonResponse({'success': True, 'message': '클래스 신청이 완료되었습니다.'})
    
    except Exception as e:
<<<<<<< HEAD
=======
        print(f"Error in 클래스신청: {e}")
>>>>>>> 5a4edcb6a4c3843af1a3137a75cee3f06ca8229b
        return JsonResponse({'success': False, 'message': f'오류가 발생했습니다: {str(e)}'})

def 출석체크(request, class_id):
    """출석 체크 화면"""
    try:
        클래스 = get_object_or_404(Class, classID=class_id)
        수강생들 = Sugang.objects.filter(class_classID=클래스).select_related('member_accountID')
        
<<<<<<< HEAD
=======
        if request.method == 'POST':
            date = request.POST.get('date')
            
            if not date:
                messages.error(request, '출석일을 선택해주세요.')
                return redirect('attendance', class_id=class_id)
            
            for 수강생 in 수강생들:
                status = request.POST.get(f'attendance_{수강생.sugangID}')
                if status:
                    Attendance.objects.update_or_create(
                        sugang_sugangID=수강생,
                        attendDate=date,
                        defaults={'attendanceStatus': status}
                    )
            
            messages.success(request, '출석이 저장되었습니다.')
            return redirect('attendance', class_id=class_id)
        
>>>>>>> 5a4edcb6a4c3843af1a3137a75cee3f06ca8229b
        return render(request, 'attendance.html', {
            'class': 클래스,
            '수강생들': 수강생들
        })
        
    except Exception as e:
<<<<<<< HEAD
=======
        print(f"Error in 출석체크: {e}")
>>>>>>> 5a4edcb6a4c3843af1a3137a75cee3f06ca8229b
        messages.error(request, '출석 체크 페이지를 불러오는 중 오류가 발생했습니다.')
        return redirect('classes')

def 게시글작성(request, class_id):
    """게시글 작성 화면"""
    if 'member_id' not in request.session:
        messages.error(request, '로그인이 필요합니다.')
        return redirect('login')
    
    try:
        클래스 = get_object_or_404(Class, classID=class_id)
        member = get_object_or_404(Member, accountID=request.session['member_id'])
        
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.class_classID = 클래스
                post.author = member
                post.save()
                messages.success(request, '게시글이 작성되었습니다.')
                return redirect('post_list', class_id=class_id)
<<<<<<< HEAD
=======
            else:
                messages.error(request, '게시글 작성 중 오류가 발생했습니다. 입력 내용을 확인해주세요.')
>>>>>>> 5a4edcb6a4c3843af1a3137a75cee3f06ca8229b
        else:
            form = PostForm()
        
        return render(request, 'post_create.html', {
            'form': form,
            'class': 클래스
        })
        
    except Exception as e:
<<<<<<< HEAD
=======
        print(f"Error in 게시글작성: {e}")
>>>>>>> 5a4edcb6a4c3843af1a3137a75cee3f06ca8229b
        messages.error(request, '게시글 작성 페이지를 불러오는 중 오류가 발생했습니다.')
        return redirect('post_list', class_id=class_id)

def 마이페이지(request):
    """마이페이지 화면"""
    if 'member_id' not in request.session:
        messages.warning(request, '로그인이 필요합니다.')
        return redirect('login')
    
    try:
        member = get_object_or_404(Member, accountID=request.session['member_id'])
        
        # 관련 데이터 조회
        신청클래스들 = Sugang.objects.filter(member_accountID=member).select_related('class_classID')
        작성게시글들 = Post.objects.filter(author=member).select_related('class_classID').order_by('-writeDate')[:10]
        관심사들 = MemberInterests.objects.filter(member=member).select_related('interests')
<<<<<<< HEAD
        출석이력 = []
=======
        출석이력 = Attendance.objects.filter(
            sugang_sugangID__member_accountID=member
        ).select_related('sugang_sugangID__class_classID').order_by('-attendDate')[:20]
>>>>>>> 5a4edcb6a4c3843af1a3137a75cee3f06ca8229b
        
        return render(request, 'mypage.html', {
            'member': member,
            '신청클래스들': 신청클래스들,
            '작성게시글들': 작성게시글들,
            '관심사들': 관심사들,
            '출석이력': 출석이력
        })
        
    except Exception as e:
<<<<<<< HEAD
=======
        print(f"Error in 마이페이지: {e}")
>>>>>>> 5a4edcb6a4c3843af1a3137a75cee3f06ca8229b
        messages.error(request, '마이페이지를 불러오는 중 오류가 발생했습니다.')
        return redirect('classes')

def 게시글목록(request, class_id):
    """게시글 목록 보기 화면"""
    try:
        클래스 = get_object_or_404(Class, classID=class_id)
        게시글들 = Post.objects.filter(class_classID=클래스).select_related('author').order_by('-writeDate')
        
        # 페이지네이션
        paginator = Paginator(게시글들, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        
        return render(request, 'post_list.html', {
            'class': 클래스,
            '게시글들': page_obj
        })
        
    except Exception as e:
<<<<<<< HEAD
=======
        print(f"Error in 게시글목록: {e}")
>>>>>>> 5a4edcb6a4c3843af1a3137a75cee3f06ca8229b
        messages.error(request, '게시글 목록을 불러오는 중 오류가 발생했습니다.')
        return redirect('classes')

def 게시글상세(request, post_id):
    """게시글 상세 보기"""
    try:
        게시글 = get_object_or_404(Post, postID=post_id)
        
        return render(request, 'post_detail.html', {
            '게시글': 게시글
        })
        
    except Exception as e:
<<<<<<< HEAD
=======
        print(f"Error in 게시글상세: {e}")
>>>>>>> 5a4edcb6a4c3843af1a3137a75cee3f06ca8229b
        messages.error(request, '게시글을 불러오는 중 오류가 발생했습니다.')
        return redirect('classes')

def 관심사별_모임(request, interest_id):
    """특정 관심사의 모임 목록"""
    try:
        interest = get_object_or_404(Interests, interestID=interest_id)
        classes = Class.objects.filter(
            interestID=interest
        ).annotate(member_count=Count('sugang_set', distinct=True)).order_by('-member_count')
        
        return render(request, 'interest_classes.html', {
            'interest': interest,
            'classes': classes
        })
        
    except Exception as e:
<<<<<<< HEAD
        messages.error(request, '관심사별 모임을 불러오는 중 오류가 발생했습니다.')
        return redirect('classes')
=======
        print(f"Error in 관심사별_모임: {e}")
        messages.error(request, '관심사별 모임을 불러오는 중 오류가 발생했습니다.')
        return redirect('classes')

def 홈페이지(request):
    """홈페이지"""
    return redirect('classes')

def 오류페이지(request, exception=None):
    """오류 페이지"""
    return render(request, 'error.html', {
        'error_message': '페이지를 찾을 수 없습니다.'
    }, status=404)
>>>>>>> 5a4edcb6a4c3843af1a3137a75cee3f06ca8229b
